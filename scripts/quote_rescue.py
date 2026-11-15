#!/usr/bin/env python3
"""Quote rescue pass: re-verify claims whose quote failed the merge attachment.

For each unverified claim in research/claims_index.json:
1. Resolve the source's page file (direct path, then substring glob).
2. Try to attach the claim's own quote to the source id verbatim.
3. If the page file is missing, search ALL saved page files for the collapsed
   quote; attach only if the match is unique AND the finding page belongs to
   the same source's theme (guards against misattribution).
4. Rewrite claims_index.json with updated quote_verified flags.
Never massages a quote; failures stay failures.
"""
import json
import sys
from pathlib import Path

SKILL = Path.home() / ".hermes/skills/research/grounded-citations/scripts"
sys.path.insert(0, str(SKILL))
import sources  # noqa: E402

PROJ = Path("/home/walker/projects/scutellaria-research")
LEDGER = PROJ / "citations" / "ledger.json"
CLAIMS = PROJ / "research" / "claims_index.json"
MASTER = PROJ / "research" / "master_map.json"


def resolve_page_file(pf: str):
    if not pf:
        return None
    p = Path(pf)
    if not p.is_absolute():
        p = PROJ / p
    if p.exists() and p.stat().st_size > 0:
        return p
    hint = Path(pf).name
    if hint:
        for cand in (PROJ / "research").glob(f"*/pages/*{hint[:40]}*"):
            if cand.stat().st_size > 0:
                return cand
    return None


def main():
    claims = json.loads(CLAIMS.read_text(encoding="utf-8"))
    master = json.loads(MASTER.read_text(encoding="utf-8"))
    by_url = {v["url"]: v for v in master.values()}

    all_pages = list((PROJ / "research").glob("*/pages/*.txt"))
    rescued, still_failed = [], []

    for c in claims:
        if c.get("quote_verified"):
            continue
        meta = by_url.get(c["url"])
        if not meta:
            still_failed.append((c.get("id"), c["claim"][:70], "no master meta"))
            continue
        quote = " ".join((c.get("quote") or "").split())
        if not quote or len(quote.split()) < 3:
            c["quote_verified"] = False
            still_failed.append((c["id"], c["claim"][:70], "quote too short"))
            continue

        page = resolve_page_file(meta.get("page_resolved") or meta.get("page_file", ""))
        attached = False
        if page:
            ev = page.read_text(encoding="utf-8")
            try:
                sources.attach_quote(LEDGER, meta["id"], quote, ev)
                attached = True
            except SystemExit:
                attached = False
        if attached:
            c["quote_verified"] = True
            c["quote_source_file"] = str(page)
            rescued.append((c["id"], c["claim"][:70], "own page"))
            continue

        # page missing or quote not in it: search all pages for the collapsed quote
        needle = " ".join(quote.split()).casefold()
        hits = []
        for p in all_pages:
            try:
                txt = " ".join(p.read_text(encoding="utf-8").split()).casefold()
            except Exception:
                continue
            if needle in txt:
                hits.append(p)
        if len(hits) == 1:
            theme_dir = hits[0].parent.parent.name
            if theme_dir in (c.get("theme", ""),) or not c.get("theme"):
                ev = hits[0].read_text(encoding="utf-8")
                try:
                    sources.attach_quote(LEDGER, meta["id"], quote, ev)
                    c["quote_verified"] = True
                    c["quote_source_file"] = str(hits[0])
                    rescued.append((c["id"], c["claim"][:70], f"unique page match: {hits[0].name}"))
                    continue
                except SystemExit:
                    pass
            else:
                still_failed.append((c["id"], c["claim"][:70], f"unique hit in OTHER theme dir {theme_dir}"))
                continue
        elif len(hits) > 1:
            still_failed.append((c["id"], c["claim"][:70], f"ambiguous: {len(hits)} pages contain quote"))
            continue
        else:
            still_failed.append((c["id"], c["claim"][:70], "quote not found in any saved page"))
        c["quote_verified"] = False

    CLAIMS.write_text(json.dumps(claims, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rescued: {len(rescued)}")
    for r in rescued:
        print("  RESCUED", r)
    print(f"still failed: {len(still_failed)}")
    for f in still_failed:
        print("  FAILED ", f)


if __name__ == "__main__":
    main()
