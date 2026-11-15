# Research Dossier 04 — Cellular Senescence, Telomeres, Model Organisms, and Aging-Disease Models for *Scutellaria baicalensis* Constituents

Scope: baicalein, baicalin, wogonin. Prepared 2026-11-14. Verbatim quotes below are exact substrings of saved page texts in `research/senescence/pages/`; structured findings and quotes are in `research/findings_senescence.json`. Thirty-eight sources were fetched and saved; every footnote refers to a saved page file.

## 1. Overview

Five published studies (2013–2025) report that baicalein extends lifespan in *Caenorhabditis elegans*, with effect sizes from roughly 10% (median lifespan, 2025) to 45–57% (mean and median, 2013), plus one positive *Drosophila* study.[^1][^2][^3][^4][^5][^6] The brief's hint verifies cleanly in baicalein's favor: no published study extends lifespan with baicalin or wogonin, and the only direct lifespan test of those two compounds — a 2026 *Drosophila* study of *Scutellaria lateriflora* (American skullcap, a different species) — found no lifespan extension.[^7]

Senescence evidence splits by context. In normal stressed cells (astrocytes, lung fibroblasts, chondrocytes, dermal fibroblasts), constituents delay senescence and suppress the senescence-associated secretory phenotype (SASP): senescence-delay plus senomorphic activity.[^13][^14][^15][^16][^17][^24][^28] In activated hepatic stellate cells and cancer cells the same molecules *induce* senescence as a therapeutic mechanism (pro-senescence).[^18][^19][^20] No Scutellaria constituent has experimental senolytic data — baicalein appears only on an in-silico candidate list.[^22] Telomerase inhibition is documented but oncology-only.[^20][^23] No human study measures senescence, telomere, or lifespan endpoints; the nearest human data are knee-osteoarthritis trials of flavocoxid, a proprietary baicalin-plus-catechin combination product.[^37][^38]

Classification used below: senolytic = selective killing of senescent cells; senomorphic = SASP suppression without removing senescent cells; senescence-delay = preventing or reversing senescence entry; pro-senescence = therapeutically inducing senescence in activated or malignant cells.

## 2. Evidence in depth

### 2.1 *C. elegans* lifespan (strain, dose, effect size)

**2013 (J Agric Food Chem).** Baicalein activated Nrf2 in Hct116 cells and the Nrf2 homolog SKN-1 in intestinal nuclei of worms; dose not stated in abstract.[^1]

> Lifespan analysis revealed that baicalein extends the mean, median, and maximum lifespans of the nematode by 45, 57 and 24%, respectively.[^1]

**2016 (Fitoterapia).** Baicalein dose-dependently prolonged life span and enhanced resistance to lethal heat and sodium arsenite; SKN-1 RNAi abolished both effects, while baicalein caused no DAF-16::GFP nuclear translocation and still induced longevity in a DAF-16 loss-of-function strain — SKN-1-dependent, DAF-16-independent.[^2]

**2021 (Antioxidants).** Head-to-head test of six structurally related flavones at 100 µM (0.4% DMSO vehicle; Lifespan Machine, 25 °C): baicalein prolonged lifespan by up to 18.6% (6-hydroxyflavone 11.8%, chrysin 8.5%), dependent on SKN-1/Nrf2; microarray showed baicalein downregulates age-related genes mTOR and PARP. Baicalin and wogonin were not among the six compounds tested.[^3]

**2023 (Life Sci).** Baicalein downregulated Wnt ligands and upregulated the GATA factor ELT-3 and an antiaging Klotho gene; lifespan enhancement required ELT-3 and SKN-1, oxidative-stress protection required ELT-3 and DAF-16; lipofuscin, ROS, and functional declines were ameliorated.[^5]

**2025 (MedComm).** The most rigorous study: wild-type N2 plus seven mutant and three reporter strains, 100 µM baicalein versus 0.1% DMSO vehicle on NGM/OP50; median lifespan rose from 20 to 22 days across three independent assays. Dietary-restriction confounds were ruled out (no OP50 growth inhibition, no feeding-preference change); mechanism localized to DAF-2/insulin-IGF-1 suppression, DAF-16 nuclear translocation, and sod-3 upregulation; supplementary data show no baicalein-induced SKN-1 translocation.[^4]

The pathway attribution is genuinely contested — SKN-1 without DAF-16 (2016, 2021) versus DAF-16 without SKN-1 (2025) versus ELT-3 plus SKN-1 for lifespan with DAF-16 for stress only (2023) — but the lifespan effect itself replicates in every study.

### 2.2 *Drosophila*

In female flies, baicalein at 0.04 and 0.2 mg/mL in food extended mean and maximum lifespan in a natural aging model and reduced oxidative damage (ROS, MDA, GSSG) in hydrogen-peroxide- and paraquat-induced aging models.[^6] Conversely, *S. lateriflora* extracts (aqueous and ethanol, 1–5 mg/mL) fed from middle age improved mobility mainly via baicalin and sleep via a wogonin mix, but:[^7]

> Since neither the extracts nor the compounds extend the lifespan, this suggests that they improve neuronal health and function and do not generally slow down the aging process.[^7]

The 5 mg/mL ethanol extract was poorly tolerated and shortened median lifespan — the only published lifespan test of baicalin or wogonin is null.[^7]

### 2.3 Cellular senescence and SASP

**Senescence-delay / senomorphic (normal stressed cells).** Baicalein protected T98G human astrocytes and primary rat astrocytes from H2O2-induced senescence, suppressing SASP secretion (IL-6, IL-8, TNF-α, CXCL1, MMP-1) via JAK2/STAT1/NF-κB inhibition plus leucine-metabolism regulation (BCAT1 down, SLC7A5 up).[^13] In bleomycin-induced lung fibrosis (ICR mice; 100 mg/kg/day oral), baicalein attenuated fibroblast senescence markers (p53, p21, p16, MCP-1, PAI-1, TNF-α, MMP-10/12) and collagen deposition (27.29% vs 4.14% in controls) through Sirt3 restoration; Sirt3 siRNA abolished the effect.[^16] Wogonin protected against bleomycin pulmonary fibrosis by inhibiting CDK9/p53-mediated senescence (γ-H2AX, phospho-p53, p21, pRB, SA-β-gal attenuated), as a direct selective CDK9 inhibitor.[^17] Wogonin attenuated chondrocyte senescence in DMM osteoarthritis mice and IL-1β-induced C28/I2 cells (SA-β-gal, SASP, γ-H2A.X, p16, p21, p53 reduced) with STAT3 as direct target.[^24] Extract-level: *S. baicalensis* ethanol extract delayed low-glucose-induced astrocyte senescence (SA-β-gal, IL-6/CXCL1/MMP-1, p16INK4A, p21, γH2A.X down).[^15]

**Constituent caveat.** A screen of 17 flavonoids isolated from Scutellaria radix found five potent SASP inhibitors — oroxylin A and 2'-hydroxylated flavones, *not* baicalein, baicalin, or wogonin — acting through IκBζ/C/EBPβ:[^14]

> compounds 8 and 11, the strongest SASP inhibitors, decreased the expression of IκBζ and C/EBPβ protein without affecting either BrdU uptake or the expression of senescence markers, such as pRb and p21.[^14]

That is textbook senomorphic action (SASP suppression without touching the arrest). Orally, compound 8 (2',5,7-trihydroxyflavone) at 2 and 4 mg/kg/day for 10 days inhibited SASP and IκBζ gene expression in kidneys of 21-month-old rats.[^14] SASP benefit from the whole plant may ride on minor constituents rather than the three headline flavones.

**Pro-senescence (therapeutic induction).** Baicalein induced senescence in activated hepatic stellate cells — G1 arrest via CEBPZ/p53/HK2-mediated glycolysis inhibition — attenuating CCl4 liver fibrosis; pifithrin-α (p53 inhibitor) abolished the anti-fibrotic effect.[^18] Baicalin induced senescence in colon cancer cells via DEPP upregulation with Ras/Raf/MEK/ERK and p16INK4A/Rb activation, suppressing xenograft growth;[^19] in parallel work, baicalin-induced senescence was attributed to telomerase reverse transcriptase inhibition while baicalein induced apoptosis in the same models.[^20] Directionality is cell-line dependent — in MC38/CT26 cells baicalin *suppressed* CDKN2A (p16) protein expression.[^21]

**Senolytic status: none.** Fingerprint screening of 40,383 natural and semi-synthetic products against reference senolytics flagged baicalein among six candidates, with the authors stating experimental validation is needed; no published experiment demonstrates selective killing of senescent cells by any Scutellaria constituent.[^22]

### 2.4 Telomeres and telomerase

Wogonin and aqueous *S. baicalensis* extract inhibited hTERT, hTP1, and c-myc mRNA and down-regulated telomerase activity in HL-60 leukemia cells; the same paper shows baicalin and wogonoside are converted to baicalein and wogonin by β-glucuronidase — relevant to oral bioactivation.[^23] Baicalin-induced senescence in colon cancer cells is attributed to telomerase reverse transcriptase inhibition.[^20] All telomere/telomerase data are oncology findings; no data exist on telomere-length maintenance in normal or aging cells.

### 2.5 Rodent aging models

**SAMP8 (senescence-accelerated, dementia-prone).** Baicalein reduced the senescence grading score, improved spatial learning, object recognition, and olfactory memory, and suppressed cortical IL-6, IL-1β, and TNF-α, with microbiome shifts correlated to cognition and cytokines;[^8] follow-up showed baicalein prevented cortical JAK2/STAT1 activation and decreased Aβ1-42 and RAGE.[^9]

**D-galactose models.** Baicalein improved novel-object-recognition and Morris-water-maze performance and inhibited NO, IL-6, IL-1β, TNF-α release;[^11] apigenin plus baicalein improved spatial memory and hippocampal/thoracic-aortic histopathology via AGEs/RAGE/NF-κB inhibition (authors report "almost equal anti-aging efficacy," but no baicalein-only arm).[^12]

**Natural aging.** In aged male Wistar rats, baicalein improved pro-oxidant/antioxidant profiles, membrane-transporter alterations, and eryptosis — proposed as a caloric-restriction mimetic candidate; no lifespan endpoint.[^10] A standardized *S. baicalensis* + *Acacia catechu* composition (UP446; 100 and 200 mg/kg oral) protected CD-1 mice against d-galactose-induced immunosenescence over 10 weeks.[^31]

### 2.6 Aging-related disease models

**Osteoarthritis.** Wogonin attenuated chondrocyte senescence in DMM mice via STAT3/PIM1;[^24] in the same model it bound histone demethylase LSD1/KDM1A, blocking NF-κB p65 demethylation, shifting synovial macrophages M1→CD163+ M2, reducing serum IL-6, improving cartilage and subchondral bone.[^25] Baicalin reduced IL-6, TNF, CXCL1, CXCL10, iNOS, MMP3, MMP13 and raised aggrecan/collagen-II in IL-1β-stimulated human chondrocytes via NF-κB inhibition, confirmed in OA mice.[^26]

**Skin photoaging.** Oral baicalein (10 and 30 mg/kg twice daily) suppressed UVB-induced skin thickening, improved elasticity, reduced tumor number/growth, and lowered IL-1β, IL-6, MCP-1, MIF, VEGF, p53, COX-2, NF-κB in hairless mice irradiated three times weekly for 23 weeks.[^27] Topical baicalin reduced epidermal thickening, raised collagen I/III, lowered MMP-1/3 in mouse skin, and in UVB-irradiated human dermal fibroblasts decreased SA-β-gal, G1 arrest, p16, p21, p53, γ-H2AX.[^28] Whole-plant: *S. baicalensis* extract antagonized REV-ERBα and up-regulated the clock gene BMAL1, protecting against d-galactose + UVB skin aging (lower MMP-1/p53, higher collagen).[^30]

**Alzheimer's-type pathology.** Wogonin promoted Aβ clearance via mTOR/autophagy and reduced tau phosphorylation via GSK3β in SH-SY5Y-APP/BACE1 cells and primary astrocytes;[^29] baicalein's SAMP8 Aβ1-42/RAGE data extend this to an aging mouse model.[^9]

**Bone.** In vitro, baicalein partially reversed glucocorticoid-induced osteoporosis markers in MC3T3-E1 cells via AKT inhibition with FOXO1 upregulation (ALP, OCN, Runx2, Col 1, mineralization).[^32] In vivo, oral baicalein at 10 mg/kg for 13 weeks showed no musculoskeletal benefit in ovariectomized estrogen-deficient rats:[^33]

> Oral administration of Baicalein did not confirm the reported favorable cortical effects in neither vertebra nor femur.[^33]

and baicalein + zileuton induced even more bone loss; the earlier positive bone findings used subcutaneous baicalein — route, dose, and model determine the outcome.[^33]

### 2.7 The epigenetic bridge

Four constituent–epigenetic-enzyme interactions are directly demonstrated, though in fibrosis, cancer, and osteoarthritis contexts rather than senescence models. Baicalein targeted DNMT1, reducing methylation of the SCARA5 promoter CpG island, derepressing SCARA5 and suppressing GPX4, driving hepatic stellate cell ferroptosis.[^34] Baicalein bound adenosylhomocysteinase (AHCY; residues D134/D303), inhibiting histone H3 lysine 4 trimethylation in microsatellite-instability colorectal cancer.[^36] Wogonin stabilized TET2, increasing 5hmC and promoting DNA demethylation via an AMPK-TET2 axis in ovarian cancer.[^35] Wogonin bound LSD1/KDM1A in osteoarthritic joints, blocking p65 demethylation and NF-κB activation — an epigenetic mechanism inside an aging-related disease model.[^25] NOT found: any study of Scutellaria constituents altering p16/CDKN2A promoter methylation, the specific hinted bridge.

## 3. Human evidence

No human study of Scutellaria constituents measures senescence, SASP, telomere, telomerase, or lifespan endpoints. The nearest human data are for flavocoxid (Limbrel), a medical food combining baicalin from *S. baicalensis* with catechins from *Acacia catechu*: in a 1-month double-blind randomized pilot study (n=103; 500 mg twice daily), flavocoxid was as effective as naproxen (500 mg twice daily) on knee-osteoarthritis signs and symptoms;[^37] a US claims cohort (3,337 flavocoxid vs 6,674 propensity-matched NSAID users) found no significant excess of hospitalized liver injury (3.2 vs 2.4 per 1,000 person-years) and a lower gastrointestinal-bleeding rate (5.3 vs 10.2 per 1,000 person-years).[^38] This is combination-product evidence for an aging-related disease, not constituent-level senescence evidence.

## 4. What is NOT established (gaps and failed hints)

1. **Senolytic activity — NOT FOUND.** No experiment shows selective killing of senescent cells by baicalein, baicalin, or wogonin; baicalein is an in-silico candidate only, explicitly unvalidated.[^22]
2. **Baicalein effects on p16 promoter methylation (hinted bridge) — NOT FOUND.** DNMT1, AHCY, TET2, and LSD1 mechanisms exist, none demonstrated in senescence or aging models.[^34][^35][^36][^25]
3. **Telomeres in normal aging cells — NOT FOUND.** hTERT/telomerase findings are leukemia and colon-cancer findings; telomere-length maintenance in normal cells is unstudied.[^20][^23]
4. **Baicalin or wogonin lifespan — NOT FOUND.** No published lifespan extension; the single direct test (*Drosophila*, 2026) is null for both compounds.[^7][^3]
5. **SAMP8 for baicalin/wogonin — NOT FOUND.** SAMP8 studies are baicalein-only.[^8][^9]
6. **Mammalian lifespan — NOT FOUND.** No mouse or rat lifespan study exists for any Scutellaria constituent; rodent data are biomarkers, senescence-accelerated, or induced-aging models.
7. **No translatable dosing.** Elegans plate exposure (100 µM) and fly food (0.04–0.2 mg/mL) versus rodent gavage (10–100 mg/kg) lack pharmacokinetic bridging.

## 5. Key sources

- MedComm 2025 (PMID 41415716) — definitive *C. elegans* lifespan study: dose, vehicle, mutants, dietary-restriction controls; full text saved.[^4]
- Antioxidants 2021 (PMID 33809299) — head-to-head flavone comparison, +18.6%, mTOR/PARP downregulation; full text saved.[^3]
- Phytomedicine 2020 (PMID 32554301) — 17-constituent SASP screen with in-vivo confirmation in aged rats.[^14]
- ACS Chem Neurosci 2021 (PMID 34152720) — cleanest baicalein senescence-delay mechanism paper.[^13]
- Phytomedicine 2025 (PMID 41075517) vs Front Pharmacol 2024 (PMID 39040475) — pro- versus anti-senescence contrast (baicalein induces stellate-cell senescence; wogonin blocks lung senescence).[^18][^17]
- Phytomedicine 2010 (PMID 19577445) — telomerase anchor (wogonin, HL-60).[^23]
- Phytomedicine 2026 (PMID 41722125) and 2025 (PMID 40818185) — wogonin chondrocyte senescence and its LSD1 epigenetic mechanism.[^24][^25]
- Front Endocrinol 2021 (PMID 34354672) — negative oral-baicalein bone study.[^33]
- Nutr Res 2009 (PMID 19555810) — human OA randomized trial of the baicalin-containing product.[^37]
- Int J Mol Sci 2026 (PMID 41516334) — honest null lifespan result for baicalin/wogonin; full text saved.[^7]

## 6. Open questions for the parent

1. **Pathway conflict.** SKN-1 (2016, 2021) versus DAF-16 (2025) attribution for baicalein's lifespan effect — recommend phrasing "multiple longevity-relevant pathways implicated; effect replicates, mechanism contested."
2. **Pro- versus anti-senescence framing.** Constituents delay senescence in normal cells yet induce it in activated stellate cells and cancer cells; a clinician audience needs this explicit to avoid "Scutellaria fights senescence" oversimplification.
3. **Constituent attribution.** Strongest SASP inhibitors are minor constituents (oroxylin A, 2'-hydroxyflavones), supporting whole-extract framing over baicalein-only claims.
4. **Human evidence ceiling.** Only product-level (baicalin+catechin) OA trials exist; no human senescence or longevity endpoints.
5. **The negative bone study.** If the paper discusses bone, oral baicalein (10 mg/kg) failed in OVX rats — route and dose matter.[^33]
6. **The baicalin/wogonin bound.** The 2026 *Drosophila* null is the only direct lifespan test of baicalin/wogonin; use it to bound claims about "Scutellaria constituents" writ large.[^7]
7. **Epigenetic division of labor.** This stream contributes senescence-adjacent epigenetic mechanisms (DNMT1, TET2, LSD1, AHCY); the epigenetics stream (brief-02) carries the deeper methylation/histone story — the two evidence bodies do not yet intersect in a single experiment.

---

## Footnotes

[^1]: Molecular effects of baicalein in Hct116 cells and Caenorhabditis elegans : activation of the Nrf2 signaling pathway and prolongation of lifespan — https://pubmed.ncbi.nlm.nih.gov/23339711/, accessed 2026-11-14.
[^2]: Baicalein modulates stress-resistance and life span in C. elegans via SKN-1 but not DAF-16 — https://pubmed.ncbi.nlm.nih.gov/27370100/, accessed 2026-11-14.
[^3]: Flavonoids' Effects on Caenorhabditis elegans' Longevity, Fat Accumulation, Stress Resistance and Gene Modulation Involve mTOR, SKN-1 and DAF-16 — https://pubmed.ncbi.nlm.nih.gov/33809299/, accessed 2026-11-14.
[^4]: Baicalein Enhances Longevity and Healthspan of C. elegans Through the Insulin/IGF-1 Signaling Pathway — https://pubmed.ncbi.nlm.nih.gov/41415716/, accessed 2026-11-14.
[^5]: Baicalein mitigates oxidative stress and enhances lifespan through modulation of Wnt ligands and GATA factor: ELT-3 in Caenorhabditis elegans — https://pubmed.ncbi.nlm.nih.gov/37463652/, accessed 2026-11-14.
[^6]: [Baicalein prolongs the lifespan of Drosophila melanogaster through antioxidation activity] — https://pubmed.ncbi.nlm.nih.gov/29924517/, accessed 2026-11-14.
[^7]: Scutellaria lateriflora Extract Supplementation Provides Resilience to Age-Related Phenotypes in Drosophila melanogaster — https://pubmed.ncbi.nlm.nih.gov/41516334/, accessed 2026-11-14.
[^8]: Effects of Baicalein on Cortical Proinflammatory Cytokines and the Intestinal Microbiome in Senescence Accelerated Mouse Prone 8 — https://pubmed.ncbi.nlm.nih.gov/29668250/, accessed 2026-11-14.
[^9]: Integration of transcriptomics and network analysis deciphers the mechanisms of baicalein in improving learning and memory impairment in senescence-accelerated mouse prone 8 (SAMP8) — https://pubmed.ncbi.nlm.nih.gov/31715136/, accessed 2026-11-14.
[^10]: Baicalein May Act as a Caloric Restriction Mimetic Candidate to Improve the Antioxidant Profile in a Natural Rodent Model of Aging — https://pubmed.ncbi.nlm.nih.gov/35316094/, accessed 2026-11-14.
[^11]: Baicalein Exerts Beneficial Effects in d-Galactose-Induced Aging Rats Through Attenuation of Inflammation and Metabolic Dysfunction — https://pubmed.ncbi.nlm.nih.gov/28548620/, accessed 2026-11-14.
[^12]: Apigenin and baicalein ameliorate thoracic aortic structural deterioration and cognitive deficit via inhibiting AGEs/RAGE/NF-κB pathway in D-galactose-induced aging rats — https://pubmed.ncbi.nlm.nih.gov/38795756/, accessed 2026-11-14.
[^13]: Baicalein Delays H(2)O(2)-Induced Astrocytic Senescence through Inhibition of Senescence-Associated Secretory Phenotype (SASP), Suppression of JAK2/STAT1/NF-κB Pathway, and Regulation of Leucine Metabolism — https://pubmed.ncbi.nlm.nih.gov/34152720/, accessed 2026-11-14.
[^14]: Flavonoids from Scutellaria baicalensis inhibit senescence-associated secretory phenotype production by interrupting IκBζ/C/EBPβ pathway: Inhibition of age-related inflammation — https://pubmed.ncbi.nlm.nih.gov/32554301/, accessed 2026-11-14.
[^15]: Unveiling the anti-senescence effects and senescence-associated secretory phenotype (SASP) inhibitory mechanisms of Scutellaria baicalensis Georgi in low glucose-induced astrocytes based on boolean network — https://pubmed.ncbi.nlm.nih.gov/35202958/, accessed 2026-11-14.
[^16]: Baicalein attenuates bleomycin-induced lung fibroblast senescence and lung fibrosis through restoration of Sirt3 expression — https://pubmed.ncbi.nlm.nih.gov/36815239/, accessed 2026-11-14.
[^17]: Wogonin protects against bleomycin-induced mouse pulmonary fibrosis via the inhibition of CDK9/p53-mediated cell senescence — https://pubmed.ncbi.nlm.nih.gov/39040475/, accessed 2026-11-14.
[^18]: Baicalein Induces Hepatic Stellate Cell Senescence and Attenuates Liver Fibrosis via CEBPZ/p53/HK2-Mediated Glycolysis Inhibition — https://pubmed.ncbi.nlm.nih.gov/41075517/, accessed 2026-11-14.
[^19]: Baicalin induces cellular senescence in human colon cancer cells via upregulation of DEPP and the activation of Ras/Raf/MEK/ERK signaling — https://pubmed.ncbi.nlm.nih.gov/29440765/, accessed 2026-11-14.
[^20]: Baicalein and baicalin inhibit colon cancer using two distinct fashions of apoptosis and senescence — https://pubmed.ncbi.nlm.nih.gov/29732005/, accessed 2026-11-14.
[^21]: Baicalin Prevents Colon Cancer by Suppressing CDKN2A Protein Expression — https://pubmed.ncbi.nlm.nih.gov/38941045/, accessed 2026-11-14.
[^22]: Natural Products as a Major Source of Candidates for Potential Senolytic Compounds obtained by in silico Screening — https://pubmed.ncbi.nlm.nih.gov/36278464/, accessed 2026-11-14.
[^23]: Wogonin, an active compound in Scutellaria baicalensis, induces apoptosis and reduces telomerase activity in the HL-60 leukemia cells — https://pubmed.ncbi.nlm.nih.gov/19577445/, accessed 2026-11-14.
[^24]: Wogonin ameliorates osteoarthritis by targeting the STAT3/PIM1 axis to attenuate chondrocyte senescence — https://pubmed.ncbi.nlm.nih.gov/41722125/, accessed 2026-11-14.
[^25]: Wogonin modulates macrophage polarization and inflammatory signaling through the LSD1-p65 axis to alleviate osteoarthritis — https://pubmed.ncbi.nlm.nih.gov/40818185/, accessed 2026-11-14.
[^26]: Baicalin Inhibits Inflammatory Responses to Interleukin-1β Stimulation in Human Chondrocytes — https://pubmed.ncbi.nlm.nih.gov/28829242/, accessed 2026-11-14.
[^27]: Baicalein prevents skin damage, tumorigenesis and tumor growth in chronic ultraviolet B-irradiated hairless mice — https://pubmed.ncbi.nlm.nih.gov/40095355/, accessed 2026-11-14.
[^28]: The protective effect of baicalin against UVB irradiation induced photoaging: an in vitro and in vivo study — https://pubmed.ncbi.nlm.nih.gov/24949843/, accessed 2026-11-14.
[^29]: Wogonin increases β-amyloid clearance and inhibits tau phosphorylation via inhibition of mammalian target of rapamycin: potential drug to treat Alzheimer's disease — https://pubmed.ncbi.nlm.nih.gov/25596147/, accessed 2026-11-14.
[^30]: Scutellaria baicalensis Georgi regulates REV-ERBα/BMAL1 to protect against skin aging in mice — https://pubmed.ncbi.nlm.nih.gov/36249807/, accessed 2026-11-14.
[^31]: Botanical Bioflavonoid Composition from Scutellaria baicalensis- and Acacia catechu-Protected Mice against D-Galactose-Induced Immunosenescence, and Cyclophosphamide Induced Immune Suppression — https://pubmed.ncbi.nlm.nih.gov/39339746/, accessed 2026-11-14.
[^32]: Baicalein ameliorates osteoporosis via AKT/FOXO1 signaling — https://pubmed.ncbi.nlm.nih.gov/34198266/, accessed 2026-11-14.
[^33]: Inhibition of Lipoxygenases Showed No Benefit for the Musculoskeletal System in Estrogen Deficient Rats — https://pubmed.ncbi.nlm.nih.gov/34354672/, accessed 2026-11-14.
[^34]: Baicalein facilitates hepatic stellate cell ferroptosis via the DNMT1/SCARA5/GPX4 axis — https://pubmed.ncbi.nlm.nih.gov/41270385/, accessed 2026-11-14.
[^35]: Wogonin Inhibits Ovarian Cancer by Activating the AMPK-TET2-5hmC Axis — https://pubmed.ncbi.nlm.nih.gov/39620386/, accessed 2026-11-14.
[^36]: Baicalein specifically suppresses microsatellite instability colorectal cancer by targeting adenosylhomocysteinase to inhibit histone H3 lysine 4 trimethylation-mediated cancer stemness — https://pubmed.ncbi.nlm.nih.gov/41038143/, accessed 2026-11-14.
[^37]: Flavocoxid is as effective as naproxen for managing the signs and symptoms of osteoarthritis of the knee in humans: a short-term randomized, double-blind pilot study — https://pubmed.ncbi.nlm.nih.gov/19555810/, accessed 2026-11-14.
[^38]: Comparative safety of flavocoxid vs prescription NSAIDs among osteoarthritis patients — https://pubmed.ncbi.nlm.nih.gov/32305527/, accessed 2026-11-14.
