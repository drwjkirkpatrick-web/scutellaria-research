#!/usr/bin/env python3
r"""Compile the paper and verify the RENDERED PDF (what the reader sees).

1. pdflatex twice (sources_block.tex is an \input, so no bibtex pass needed)
2. pdftotext the PDF, then:
   - every \\src{n} id in the .tex must appear as a listed source in the PDF
   - every string in research/key_facts.json (label -> needle) must be present,
     whitespace-normalized
   - no LaTeX markup may leak into the rendered text
Exit code non-zero on any failure. Prints a compact report.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

PROJ = Path("/home/walker/projects/scutellaria-research")
PAPER = PROJ / "paper"
TEX = PAPER / "scutellaria_review.tex"
PDF = PAPER / "scutellaria_review.pdf"
FACTS = PROJ / "research" / "key_facts.json"


def run(cmd, cwd=PAPER):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p


def main():
    tex_files = sorted(p for p in PAPER.glob("*.tex") if p.name != "sources_block.tex")
    tex = "\n".join(p.read_text(encoding="utf-8") for p in tex_files)
    cited = sorted({int(n) for n in re.findall(r"\\src\{(\d+)\}", tex)})
    print(f"\\src ids cited: {len(cited)} (range {cited[0] if cited else '-'}..{cited[-1] if cited else '-'})")

    for pass_no in (1, 2):
        p = run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", TEX.name])
        tail = [l for l in p.stdout.splitlines() if l.startswith("!") or "Fatal" in l]
        if p.returncode != 0 or tail:
            print("COMPILE FAILED (pass", pass_no, "):")
            print("\n".join(p.stdout.splitlines()[-40:]))
            sys.exit(1)
        print(f"pass {pass_no}: compiled, {PDF.stat().st_size // 1024} KB")

    pt = run(["pdftotext", PDF.name, "-"])
    txt = pt.stdout
    flat = " ".join(txt.split())

    failures = []

    # 1. every cited id resolves to a listed source in the rendered Sources list
    for i in cited:
        if f"[{i}]" not in flat:
            failures.append(f"cited id [{i}] not found in rendered PDF sources list")

    # 2. load-bearing facts present in the RENDERED text
    if FACTS.exists():
        facts = json.loads(FACTS.read_text(encoding="utf-8"))
        for label, needle in facts.items():
            if " ".join(needle.split()) not in flat:
                failures.append(f"key fact missing from rendered PDF: {label!r} -> {needle[:80]!r}")
    else:
        print("note: research/key_facts.json not present, skipping fact checks")

    # 3. no markup leaked
    for tok in [r"\src{", r"\textbf", r"\textit", r"\url{", r"\href{", r"\noindent"]:
        if tok in txt:
            failures.append(f"LaTeX markup leaked into rendered text: {tok}")

    # 4. sanity: page count
    pages = txt.count("\x0c")
    print(f"rendered pages: ~{pages}")

    if failures:
        print(f"VERIFY FAILED ({len(failures)}):")
        for f in failures:
            print("  FAIL:", f)
        sys.exit(1)
    print("RENDERED PDF VERIFIED: all cited ids listed, key facts present, no markup leaked")


if __name__ == "__main__":
    main()