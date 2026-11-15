# Project State: Scutellaria Longevity Research

> **Last updated:** 2026-11-14
> **Current phase:** complete
> **Overall health:** green

---

## 1. Goal (1-2 sentences)
A grounded-citations LaTeX research paper (PDF) on *Scutellaria baicalensis* (Chinese skullcap, huangqin) as a longevity botanical medicine, with epigenetic and gene-expression mechanisms as the evidentiary foundation, written for naturopathic practice and published to GitHub with its full evidence trail.

## 2. Current Status
### Done
- [x] Project scaffold: paper/, citations/, research/{6 theme dirs}/pages, scripts/, notes/, docs/
- [x] Pipeline scripts adapted from tulsi-research (merge_and_register, gen_sources_block, compile_and_verify)
- [x] Master ledger reset: citations/ledger.json
- [x] Parent seed sweep registered (16 queries, 71 unique sources in ledger, research/batch_seed.json)
- [x] Six parallel research subagents COMPLETE (deleg_5502bcb7): 34+58+38+38+38+52 stream sources, 288 page files, six dossiers (2,268-3,054 words each)
- [x] Merge: 227 unique child sources -> ledger (293 total with seed sweep); 370 quotes attached verbatim-verified
- [x] Quote rescue pass: 14/14 failed claims re-attached as genuine substrings -> 155/155 claims carry verified quotes
- [x] PMID esummary spot-check: 12/12 load-bearing records match children's metadata; Soldera 38495279 registered + quoted (id 293)
- [x] Paper written (parent only): scutellaria_review.tex + body2.tex, ~9,600 words, 182 cited ids, 3 tables
- [x] sources_block.tex generated mechanically: 182 sources, 181 with evidence quotes
- [x] Compiled clean (pdflatex x2), 45 pages, 551 KB; RENDERED PDF VERIFIED (all ids listed, all key facts present, no markup leaked)
- [x] Zero overfull hboxes (after unicode guard for ∞/μ/ζ/′/·/®/CJK + \allowbreak in \src + emergencystretch + table geometry fixes)
- [x] Citation-drift audit: 192 key-claim ids -> 0 failures
- [x] README (Phosphorus voice), Project_state.md -> phase complete

### In Progress
(none)

### Not Started
- [x] ~~Merge child findings into master ledger; mechanical verbatim-quote verification~~ (done)
- [x] ~~Parent writes paper/scutellaria_review.tex~~ (done)
- [x] ~~Generate sources_block.tex; compile pdflatex x2; rendered-PDF verification~~ (done)
- [x] ~~Citation-drift audit~~ (0/192 failures)
- [x] ~~README (Phosphorus style), git init/commit, GitHub repo + push to main~~ (this session)

## 3. Architecture & Key Decisions
| Decision | Rationale | Date |
|---|---|---|
| Tulsi-research pipeline reused wholesale (subagents research only; parent writes all prose) | proven; one voice; no ledger id collisions | 2026-11-14 |
| Epigenetics is its own dedicated research stream = the paper's foundation | user-specified framing: "epigenetic and gene expression abilities as the foundation" | 2026-11-14 |
| 6 streams: phytochemistry / epigenetics / longevity / senescence / clinical / safety | broader than tulsi's 4; epigenetics + organ-models split | 2026-11-14 |
| Children write findings_<theme>.json + saved pages; parent merges and re-verifies every quote mechanically | child self-reports are not evidence (grounded-citations pitfall) | 2026-11-14 |
| PubMed E-utilities (esearch/esummary/efetch) as primary biomedical retrieval | pubmed-botanical-research workflow; more reliable than scraping | 2026-11-14 |

## 4. Blockers & Risks
- **Risk:** epigenetics literature for Scutellaria is cancer-cell-line skewed → mitigation: dedicated child instructed to map evidence quality per finding and state where longevity framing borrows from oncology models; paper says so explicitly.
- **Risk:** children's hinted leads (e.g. C. elegans lifespan) may not survive verification → briefs demand "flag as NOT FOUND" rather than rounding.
- **Risk:** direct human longevity endpoints likely absent → paper must state the gap honestly ([unverified]/Limitations), not smooth over.

## 5. Next Step (only ONE)
> **Next:** none — project complete and pushed to GitHub.

## 6. Environment & Tooling Notes
- Host: Jetson (Linux tegra); pdflatex (TeX Live 2022), pdftotext, gh at ~/bin/gh (authed as drwjkirkpatrick-web, https protocol)
- Ledger: citations/ledger.json (sources.py global --ledger flag BEFORE subcommand, or HERMES_CITATION_LEDGER env var)
- Scripts: scripts/merge_and_register.py, scripts/gen_sources_block.py, scripts/compile_and_verify.py
- Paper: paper/scutellaria_review.tex + generated sources_block.tex
- Unicode guard in preamble is mandatory for quoted text (U+2212 etc. were fatal on tulsi first compile)

## 7. Recent Session Log
- 2026-11-14: Project created from scratch; scripts adapted; ledger reset; seed sweep; six research subagents dispatched.
- 2026-11-14: Streams merged (227 sources, 370 verbatim quotes, 155/155 claims verified); paper written and compiled (45 pp, 182 cited ids, 0 overfull, rendered-PDF verified); citation-drift audit 0/192; README + push to GitHub.

## 8. References
- Skill: research/grounded-citations (ledger + evidence discipline)
- Skill: research/research-toolkit -> grounded-latex-paper-workflow, research-fanout-dossiers, pubmed-botanical-research
- Precedent project: /home/walker/projects/tulsi-research (Holy Basil review, 105 sources)
