# Scutellaria baicalensis: A Longevity Botanical Medicine

*Chinese skullcap. Huangqin (黄芩). The golden root of the classical materia medica — and, it turns out, one of the best-mapped gene-expression botanicals in the modern literature.*

This repository holds a **grounded-citations review paper** (LaTeX → PDF) of *Scutellaria baicalensis* Georgi as a longevity botanical medicine, written for naturopathic practice, with the epigenetic and gene-expression evidence as its explicit foundation.

## The paper

**`paper/scutellaria_review.pdf`** — 45 pages, ~9,600 words, 182 cited sources, each resolving to a fetched page with most carrying a verbatim captured evidence sentence. Three tables: the epigenetic enzyme-target map, every published lifespan study, and the human trial record with its honest durations.

## What it found

The story the evidence tells is compact enough to carry in one line: *a plant whose constituents touch the cell's epigenetic machinery directly, and whose one demonstrated lifespan effect ran through an epigenetic enzyme.*

- **The foundation is real.** Baicalein induces DNMT1-mediated promoter demethylation in three independent systems; inhibits HDAC-1/8; blocks AHCY (one-carbon metabolism) to suppress H3K4me3; down-regulates the m⁶A demethylase FTO. Baicalin is a characterized LSD1 inhibitor (IC₅₀ 3.01 µM) whose target has been engaged in human metastatic tissue *ex vivo*. Wogonin down-regulates p300, stabilizes TET2, and demethylates the KEAP1 promoter. The miRNA, lncRNA, and whole-transcriptome layers complete the map.
- **The lifespan claim belongs to baicalein.** Five *C. elegans* studies (2013–2025) replicate the extension; the one genetic experiment that asked *how* found the answer in **cbp-1**, the worm ortholog of CBP/p300. Baicalin and wogonin failed their single direct test — a null result this paper carries deliberately.
- **Senomorphic, not senolytic.** SASP suppression is real (and strongest from *minor* constituents of the root — an argument for whole-extract formulations); selective killing of senescent cells has never been demonstrated.
- **The human ceiling is stated plainly.** Phase I baicalein to 2,800 mg; a 374-patient baicalin lipid/inflammation trial; flavocoxid matched naproxen twice in osteoarthritis; and *no* human longevity endpoint, *no* epigenetic-clock study — the two studies that would test this paper's thesis have never been run.
- **Safety resolves honestly.** A rare, idiosyncratic, largely blend- and suprapharmacopoeial-dose liver signal; a germander-adulteration history that owns most of "skullcap hepatotoxicity"; a 26-week GLP NOAEL at 7.5–25× the pharmacopoeial dose; and one genotype-dependent human interaction that matters (rosuvastatin AUC −47% via OATP1B1).

## How the evidence was built

Every claim was grounded at retrieval time, mechanically:

1. **Six parallel research streams** (phytochemistry, epigenetics, longevity pathways, senescence, clinical, safety), each instructed to *flag* unverifiable leads rather than round them off — several plausible-sounding claims died under verification and are recorded in the paper as not found.
2. **A retrieval ledger of 293 fetched sources** (`citations/ledger.json`), with the text of every fetched page saved under `research/*/pages/`.
3. **370+ verbatim evidence quotes**, each re-verified as an exact substring of its saved page by the parent — no child self-report was trusted.
4. **A generated Sources block** (`paper/sources_block.tex`) — never hand-typed — so citations and URLs cannot drift from the ledger.
5. **Rendered-PDF verification**: every cited id resolves in the compiled output, every key fact is present in the rendered text, zero overfull margins, no markup leakage, and a 192-id citation-drift audit passing at 100%.

## Repository layout

- `paper/` — `scutellaria_review.tex`, `body2.tex`, generated `sources_block.tex`, and the compiled PDF
- `citations/ledger.json` — the full retrieval ledger with evidence quotes
- `research/` — six stream dossiers (`01`–`06`), structured findings JSON, saved page texts per stream, and the merge/verification artifacts (`master_map.json`, `claims_index.json`, `key_facts.json`)
- `scripts/` — the pipeline: `merge_and_register.py` (mechanical verification + ledger registration), `quote_rescue.py`, `gen_sources_block.py` (ledger → LaTeX sources block), `compile_and_verify.py` (compile + rendered-PDF assertions)
- `notes/` — the six research-stream briefs, preserved as project artifacts

## Method lineage

This is the second botanical review built on this pipeline, after the Holy Basil (*Ocimum tenuiflorum*) review in [tulsi-research](https://github.com/dwjkirkpatrick-web/tulsi-research). The discipline is the same: the ledger is the only bibliography, quotes are substrings or they are dropped, and the negative space — what could not be verified — is published alongside the findings.

**Author:** Walker J. Kirkpatrick, ND · November 2026
