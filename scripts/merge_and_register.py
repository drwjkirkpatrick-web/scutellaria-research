#!/usr/bin/env python3
"""Merge subagent findings JSON into the master citation ledger.

- Loads research/findings_<theme>.json for each theme
- Dedupes URLs across themes (first occurrence wins, later themes attach theirs)
- Registers every URL in citations/ledger.json (stable, idempotent order)
- Verifies each quote verbatim against its saved page file, attaches survivors
- Emits research/master_map.json (id -> bibliography metadata) and
  research/claims_index.json (claim -> ledger id -> quote)
- Prints a compact report; problems are listed, never silently dropped
"""
import json
import sys
from pathlib import Path

PROJ = Path("/home/walker/projects/scutellaria-research")
SKILL = Path.home() / ".hermes/skills/research/grounded-citations/scripts"
sys.path.insert(0, str(SKILL))
import sources  # ledger library: add_sources, attach_quote, quote_in_evidence, normalize_url

LEDGER = PROJ / "citations" / "ledger.json"
THEMES = ["phytochemistry", "epigenetics", "longevity", "senescence", "clinical", "safety"]


def resolve_page_file(pf: str):
    if not pf:
        return None
    p = Path(pf)
    if not p.is_absolute():
        p = PROJ / p
    if p.exists() and p.stat().st_size > 0:
        return p
    # substring glob fallback (citation-pitfalls: slugs get mangled)
    hint = Path(pf).name
    if hint:
        for cand in (PROJ / "research").glob(f"*/pages/*{hint[:40]}*"):
            if cand.stat().st_size > 0:
                return cand
    return None


def as_text(v, sep="; "):
    """Coerce child-JSON field variance: None -> '', list -> joined, scalars -> str."""
    if v is None:
        return ""
    if isinstance(v, list):
        return sep.join(str(x).strip() for x in v if str(x).strip()).strip()
    if isinstance(v, (int, float)):
        return v
    return str(v).strip()


def main():
    master = {}          # normalized url -> meta
    claims = []
    problems = []
    theme_stats = {}

    for theme in THEMES:
        f = PROJ / f"research/findings_{theme}.json"
        if not f.exists():
            problems.append((theme, "findings file missing", str(f)))
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append((theme, "findings JSON unreadable", str(exc)))
            continue

        n_src = n_claim = 0
        for s in data.get("sources", []):
            url = (s.get("url") or "").strip()
            if not url.startswith(("http://", "https://")):
                problems.append((theme, "non-http source url skipped", url[:100]))
                continue
            key = sources.normalize_url(url)
            if key in master:
                master[key]["themes"] = sorted(set(master[key]["themes"] + [theme]))
                if s.get("quotes") and not master[key]["quotes"]:
                    master[key]["quotes"] = s["quotes"]
                continue
            master[key] = {
                "url": key,
                "raw_url": url,
                "title": as_text(s.get("title")),
                "authors": as_text(s.get("authors"), sep="; "),
                "year": s.get("year"),
                "journal_or_publisher": as_text(s.get("journal_or_publisher")),
                "vol_pages": as_text(s.get("vol_pages")),
                "doi": as_text(s.get("doi")),
                "pmid": s.get("pmid"),
                "page_file": as_text(s.get("page_file")),
                "quotes": [q for q in (s.get("quotes") or []) if isinstance(q, str) and len(q.split()) >= 3],
                "notes": as_text(s.get("notes")),
                "extract_status": s.get("extract_status") or "ok",
                "themes": [theme],
            }
            n_src += 1
        for c in data.get("claims", []):
            curl = (c.get("url") or "").strip()
            if not curl:
                continue
            claims.append({
                "claim": as_text(c.get("claim")),
                "url": sources.normalize_url(curl),
                "quote": as_text(c.get("quote")),
                "strength": c.get("strength") or "",
                "theme": theme,
            })
            n_claim += 1
        theme_stats[theme] = (n_src, n_claim)

    # --- register every unique url in stable order -------------------------
    for key, meta in master.items():
        entry = sources.add_sources(LEDGER, [meta["raw_url"]], title=(meta["title"] or None))[0]
        meta["id"] = entry["id"]
        if entry.get("title"):
            meta["title"] = entry["title"]

    # --- verify + attach quotes --------------------------------------------
    quotes_attached = 0
    for key, meta in master.items():
        page = resolve_page_file(meta["page_file"])
        meta["page_resolved"] = str(page) if page else ""
        if not page:
            meta["quotes_ok"] = []
            if meta["quotes"]:
                problems.append((meta["id"], "page file missing; quotes NOT attached", meta["page_file"][:80]))
            continue
        ev = page.read_text(encoding="utf-8")
        ok = []
        for q in meta["quotes"]:
            try:
                sources.attach_quote(LEDGER, meta["id"], q, ev)
                ok.append(q)
                quotes_attached += 1
            except SystemExit:
                problems.append((meta["id"], "quote failed verbatim check; dropped", " ".join(q.split())[:90]))
        meta["quotes_ok"] = ok

    # --- claims index -------------------------------------------------------
    claims_out = []
    for c in claims:
        meta = master.get(c["url"])
        if not meta:
            problems.append((c["theme"], "claim url not among sources", c["claim"][:80]))
            continue
        # confirm the claim's quote survived verification
        key_norm = " ".join(c["quote"].split()).casefold()
        quote_ok = any(" ".join(q.split()).casefold() == key_norm for q in meta["quotes_ok"])
        claims_out.append({**c, "id": meta["id"], "quote_verified": quote_ok})

    # dedupe identical claims (same id + near-identical text)
    seen = set()
    deduped = []
    for c in claims_out:
        k = (c["id"], " ".join(c["claim"].lower().split())[:80])
        if k in seen:
            continue
        seen.add(k)
        deduped.append(c)

    (PROJ / "research/master_map.json").write_text(
        json.dumps(master, indent=1, ensure_ascii=False), encoding="utf-8")
    (PROJ / "research/claims_index.json").write_text(
        json.dumps(deduped, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"themes: " + ", ".join(f"{t}=src:{n}+claim:{k}" for t, (n, k) in theme_stats.items()))
    print(f"unique sources registered: {len(master)}")
    print(f"quotes attached: {quotes_attached}")
    print(f"claims indexed: {len(deduped)} "
          f"(quote_verified={sum(1 for c in deduped if c['quote_verified'])})")
    print(f"problems: {len(problems)}")
    for p in problems[:25]:
        print("  PROBLEM:", p)
    ids = sorted(m["id"] for m in master.values())
    print(f"ledger id range: {ids[0] if ids else '-'}..{ids[-1] if ids else '-'}")
    unverified_quote_claims = [c for c in deduped if not c["quote_verified"]]
    print(f"claims whose quote did NOT verify (handle before citing): {len(unverified_quote_claims)}")
    for c in unverified_quote_claims[:15]:
        print("  UNVERIFIED-QUOTE CLAIM:", c["id"], c["claim"][:90])


if __name__ == "__main__":
    main()