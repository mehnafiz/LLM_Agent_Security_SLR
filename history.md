# Note — LLM-Based Agent Security Evaluation

Current record flow: 4,500 collected, 3,059 after duplicate removal, 606 kept for screening, 100 in the final set, 68 open PDFs. Those counts are in `README.md` and `SLR_Record_Flow.xlsx`.

The rest of this file is the working note through 3 November 2026. Its 434 and 419 figures are that earlier IEEE and Google Scholar bibliography, not the current collection. Ja record e nei, seta ekhane likha hoyni. Kono DOI, quartile, abstract, ba paper identity ekhane banano hoyni.

---

## 1. Research ta ki

Topic: **LLM-based agent security evaluation**.

Char ta dimension:

1. Attack
2. Evaluation metrics and benchmarks
3. Mitigation and defense (eta priority)
4. Proposed framework

Nijer framework er naam **AgentShield-LCE**. Eta design. Experiment kora hoyni. Eta kono published benchmark er rename na. AgentDojo, InjecAgent, WASP, OpenAgentSafety — egulo alada paper. Amader lifecycle ta bole ei slice gulo ek sathe, order e, gate diye kivabe use hobe.

---

## 2. Folder map — kothay ki, keno

Parent folder:

`/Users/mehnafiz/Desktop/NEW PAPER JOURNAL/new/`

| Path | Ki | Keno alada |
|------|----|------------|
| `LLM_Agent_Security_Literature_Collection.xlsx` | IEEE original workbook | Source. Edit kora hoyni |
| `Google_Scholar_Best_Related_LLM_Agent_Security.xlsx` | Scholar original workbook | Source. Edit kora hoyni |
| `TOP_RELATED_PAPER/` | Age download kora PDF, ekta paper = ekta folder | Original. Move/rename/delete kora hoyni. Copy neya hoyeche |
| `LLM_Agent_Security_SLR/` | Purono phase output (Phase 2 theke 6A.3.1) | Frozen history. FINAL er vitore copy kore "phase" banano hoyni |
| `LLM_Agent_Security_SLR_FINAL/` | Ekhon er clean project | Defence ar porer kaj er working folder |

FINAL er vitore:

| Folder | Ki rakha |
|--------|----------|
| `00_PROTOCOL/` | Objective, eligibility, protocol |
| `01_SOURCE_DATABASES/` | IEEE workbook copy, Scholar workbook copy, Crossref hit list |
| `02_SCREENING/` | Full-text register (158), IEEE Top 30 register, exclusion (9) |
| `03_SELECTED_LITERATURE/` | 14 candidate. Final inclusion na |
| `04_FULL_TEXT_PDFS/IEEE/` | 30 ta PDF, ek copy, kono inner folder nai |
| `04_FULL_TEXT_PDFS/Proceedings/` | 14 ta proceedings PDF |
| `05_LITERATURE_ANALYSIS/` | Oi 14 tar analysis matrix + `Research_Gaps.md` |
| `06_PROPOSED_FRAMEWORK/` | AgentShield-LCE likha + workflow PNG |
| `07_ZOTERO/PRE/` | Dui workbook stack, duplicate soho, 434 row |
| `07_ZOTERO/POST/` | Exact duplicate bad, 419 row + removal log + RIS |
| `08_REPORTS/` | Search, screening, venue, PRISMA-style count |
| `09_AUDIT/` | Manifest, SHA-256, decision log, validation |
| `README.md` | Short front page |
| `defence.md` | Ei file |

Zotero app e kichu import kora hoyni. `07_ZOTERO` sudhu file. PRE te merged, POST e exact duplicate removed.

---

## 3. Search — kothay, kokhon, kivabe

### 3.1 IEEE Xplore

- Date: **26 October 2026**
- Log: original IEEE workbook er `Database_Search_Log` sheet
- Copy: `01_SOURCE_DATABASES/IEEE/IEEE_Source_Collection.xlsx`
- Access: guest / normal Xplore session. Paywall bypass kora hoyni
- Collected unique rows: **164** (`All_Collected_Papers`)
- Nicher number gulo **query-wise hit**. Egulo jog kore unique paper count hoyna. Same paper onek query te ashe.

Age access check (result export 0):

- IEEE Xplore UI
- ACM Digital Library
- Scopus
- Web of Science

ACM, Scopus, Web of Science e oi din result count o ashe ni, export o 0. Tai oi tin database theke paper table banano hoyni.

IEEE query (ID, database-reported hit, exact query):

| ID | Hit | Query |
|----|----:|-------|
| IEEE-01 | 306 | `("LLM agents" OR "LLM agent" OR "LLM-based agents" OR "LLM-based agent" OR "large language model agents" OR "large language model agent") AND (security OR attack OR defense OR threat OR vulnerability OR adversarial)` |
| IEEE-02 | 149 | `"LLM agents" AND security` |
| IEEE-03 | 0 | `"large language model agents" AND "security evaluation"` |
| IEEE-04 | 4 | `"LLM agents" AND "security assessment"` |
| IEEE-05 | 59 | `("AI agents" OR "autonomous agents") AND ("large language model" OR LLM) AND security AND evaluation` |
| IEEE-06 | 16 | `"tool-augmented" AND (LLM OR "language model") AND security` |
| IEEE-07 | 127 | `("LLM agent" OR "LLM agents" OR "LLM-based agent") AND (attack OR defense)` |
| IEEE-08 | 251 | `("LLM agent" OR "LLM agents" OR "large language model") AND "multi-agent" AND (security OR attack OR adversarial OR defense)` |
| IEEE-09 | 11 | `"LLM agent" AND "attack surface"` |
| IEEE-10 | 37 | `("LLM agents" OR "LLM agent") AND "threat model"` |
| IEEE-11 | 129 | `"prompt injection" AND (agent OR agents)` |
| IEEE-12 | 39 | `"indirect prompt injection"` |
| IEEE-13 | 1 | `"agent hijacking"` |
| IEEE-14 | 13 | `"memory poisoning" AND (LLM OR agent OR agents)` |
| IEEE-15 | 6 | `"tool misuse" AND (LLM OR agent OR agents)` |
| IEEE-16 | 53 | `("LLM agent" OR "LLM agents") AND (vulnerability OR vulnerabilities)` |
| IEEE-17 | 16 | `("LLM agents" OR "LLM agent" OR "language model agent") AND (backdoor OR poisoning OR "privilege escalation")` |
| IEEE-18 | 10 | `("LLM agents" OR "LLM agent") AND ("data leakage" OR "privacy attack" OR "privacy attacks")` |
| IEEE-19 | 30 | `("LLM agents" OR "LLM agent") AND "attack success rate"` |
| IEEE-20 | 236 | `("LLM agent" OR "LLM agents") AND (benchmark OR "security evaluation")` |
| IEEE-21 | 100 | `("LLM agent" OR "LLM agents") AND (defense OR mitigation OR guardrail OR guardrails)` |
| IEEE-22 | 77 | `"prompt injection" AND (defense OR detection) AND (agent OR agents)` |
| IEEE-23 | 12 | `("systematic review" OR survey) AND security AND ("LLM agent" OR "LLM agents" OR "language model agent" OR "LLM-based agent")` |
| IEEE-24 | 103 | `"Model Context Protocol" AND (security OR attack OR vulnerability) AND (agent OR LLM)` |
| IEEE-25 | 0 | `("LLM agents" OR "LLM agent" OR "prompt injection") AND (security OR attack) AND (agent OR agents)` |
| IEEE-26 | 87 | `("large language model" OR LLM) AND (agent OR agents) AND (security OR attack OR privacy OR injection OR vulnerability OR defense OR threat OR backdoor OR poison)` |
| IEEE-27 | 30 | `"prompt injection" AND (agent OR agents OR tool OR tools OR LLM OR "language model")` |
| IEEE-28 | 5 | `("tool-using" OR "tool augmented" OR "tool-augmented" OR "tool-using language") AND ("language model" OR LLM) AND (security OR privacy OR attack OR injection)` |
| IEEE-29 | 4 | `("large language model" OR LLM) AND (agent OR agents OR agentic) AND (security OR attack OR "prompt injection" OR privacy OR backdoor OR poison OR threat OR vulnerability)` |
| IEEE-30 | 18 | `("large language model" OR LLM OR "language model") AND (agent OR agents) AND (security OR attack OR privacy OR "prompt injection" OR backdoor)` |
| IEEE-31 | 14 | `("LLM agents" OR "LLM agent" OR "LLM-based agent" OR "language model agent" OR "foundation model based agents" OR "foundation model-based agents") AND (security OR attack OR privacy OR risk OR threat OR defense OR injection)` |

IEEE workbook er screening log (historical, re-run kora hoyni):

- Include 135
- Review 29
- Exclude 788

`Top_30_Selected` sheet e 30 ta record. Relevance score, dimension, DOI, official URL oi sheet e. Oi 30 ta automatically final eligible na.

### 3.2 Google Scholar

- Date note: workbook README te **27 October 2026**. Year filter **2020–2026**
- Log sheet: `Search_Log`
- Paper table: `All_Related`, **270** row
- Copy: `01_SOURCE_DATABASES/Google_Scholar/Google_Scholar_Source_Collection.xlsx`

| Query | Year | Pages saved |
|-------|------|-------------|
| `"LLM agents" "prompt injection"` | 2020–2026 | 0–40 |
| `"indirect prompt injection" (agent OR agents)` | 2020–2026 | 0–70 |
| `"web agent" "prompt injection"` | 2020–2026 | 0–70 |
| `"LLM agents" (defense OR mitigation OR benchmark OR safeguard)` | 2020–2026 | 0–70 |
| `"multi-agent" (LLM OR "language model") (security OR privacy OR backdoor OR injection)` | 2020–2026 | 0–60 |
| `"model context protocol" (security OR attack OR injection) (agent OR LLM)` | 2020–2026 | 0–50 |
| `(backdoor OR poisoning OR "memory poisoning") ("LLM agent" OR "LLM agents" OR "language model agent")` | 2020–2026 | 0–50 |
| `("tool-using" OR "tool-integrated" OR "tool calling") LLM agent security` | 2020–2026 | 0–50 |
| `("computer-use agent" OR "computer use agent") security OR prompt injection` | 2020–2026 | 0–50 |
| `("large language model" OR LLM) (agent OR agents) security` | 2020–2024 | 0–10, tarpor ar result nai |
| `"prompt injection" (agent OR agents OR tool)` | 2020–2024 | 0–20 |
| `"LLM agent" security` | 2023–2024 | 0–30 |
| `"language model" (chatbot OR assistant) security` | 2020–2023 | 0–50; generic chatbot screen out |

Scholar snippet ke abstract dhore neya hoyni. Scholar BibTeX theke DOI parse kora hoyeche sudhu jekhane `doi =` chilo. Na thakle DOI field khali.

### 3.3 Crossref (pore, supplementary)

- Date: **3 November 2026**
- File: `01_SOURCE_DATABASES/Other_Databases/Supplementary_Crossref_Search.xlsx`
- Open Crossref API. Paywall na
- Query tin ta:
  - `LLM agent security benchmark prompt injection`
  - `MCP tool LLM agent security`
  - `multi-agent LLM security defense`
- Hit: **29** row
- Label: metadata hit. Screen kora hoyni. Include o kora hoyni. PDF download o kora hoyni ei list theke

### 3.4 Ja search kora hoyni

- Clarivate JCR
- Scopus CiteScore

License session chilo na. Tai Q1/Q2 lekha hoyni. Blank quartile ke Q1 banano hoyni.

---

## 4. Dedup — kivabe

PRE: IEEE 164 + Scholar 270 = **434**. Duplicate o rakha.

POST rule:

- DOI mile gele ek row
- DOI na thakle normalized title exact mile gele ek row
- Duita source mile gele **IEEE row rakha**, Scholar row log e
- Fuzzy / "prochur mil" title auto-merge kora hoyni

Result: **419** unique, **15** remove.

Files:

- `07_ZOTERO/PRE/Merged_IEEE_and_Scholar.xlsx`
- `07_ZOTERO/POST/Deduplicated_Literature.xlsx`
- `07_ZOTERO/POST/Duplicate_Removal_Log.xlsx`
- `07_ZOTERO/POST/Deduplicated_Literature.ris`

15 + 419 = 434. Ei hisab historical Phase 2 er "exact DOI + exact title" count er sathe mile (419). Ota re-use kora, notun kore guess kora na.

---

## 5. Historical phase — kothay, ki decision chilo

Sob `LLM_Agent_Security_SLR/` er vitore. FINAL e phase-named copy rakha hoyni, karon oi folder phase-wise na.

| Phase | Ki hoyechilo | Number (log onujayi) |
|-------|----------------|----------------------|
| Phase 2 | Master DB, exact dedup | Provisional active 419 |
| Phase 3 | 12 unresolved duplicate candidate classify. Merge execute hoyni | Confirmed duplicate 6, extension 1, poster/full 1, related distinct 4 |
| Phase 4 | Title screen of 419 | Include 370, Exclude 16, Uncertain 33. Include = abstract e jabe, final na |
| Phase 5 | Abstract screen | Include suggestion 309, Exclude 7, Uncertain 87 |
| Phase 5B | Audit. Decision change hoyni | Evidence strength A 184, B 18, C 107 |
| Phase 6A | Legal PDF retrieval | Identity-verified PDF 158. Paywalled 133. Not found 60 |
| Phase 6B | Full text of those 158 | Include suggestion 143, Exclude 9, Uncertain 6. Human confirm pending |
| Phase 6A.1–6A.2 | Publication type / venue audit | Frozen |
| Phase 6A.3 | Strict venue rule | Eligible auto-promote **0**. Pending 281, Excluded 115 |
| Phase 6A.3.1 | Pending resolution, Crossref + CORE 2023 mirror | Pending 237, Excluded 159, Eligible **0** |

6A.3 policy ja log e ache: journal er jonno JCR Q1–Q2 ba CiteScore Q1–Q2; conference er jonno main-track + CORE A*/A (ba CCF A/B) + official proceedings. Licensed quartile na thakay journal quartile **Pending** e thake.

6B Include er modhye pore check: onek PDF er source host `arxiv.org`. ArXiv-only ke final eligible kora hoyni.

---

## 6. PDF — kivabe rakha

### IEEE download

Source: `TOP_RELATED_PAPER/`. 30 ta PDF. Original folder thik ache.

Copy: `04_FULL_TEXT_PDFS/IEEE/`. Ekbar. Inner folder nai. `Txx` naam e second copy rakha hoyni, karon duplicate hochilo.

Link rule (`02_SCREENING/IEEE_Top30_Register.xlsx`):

- Folder name `02_`, `03_` emon rank prefix mile gele, ba PDF text e title mile gele → **Linked**
- Na mille → **Not linked**
- Linked: **12**
- Not linked: **18**
- Broken path: 0 (linked row er file disk e ache)

Keno 18 link hoyni: download folder er number (jaise `121_`, `48_`) Top 30 rank na. Preprint filename `PREPRINT_arxiv_not_IEEE_published.pdf` o ache. Chokh diye "ei file ei paper" bola hoyni.

Rank 12 title `[Short Paper]` diye start. Eligibility rule e short paper out. Tai oi row **Excluded**.

### Proceedings

`04_FULL_TEXT_PDFS/Proceedings/` e 14 ta PDF.

Host (master theke, verified DOI na): `aclanthology.org`, `proceedings.iclr.cc`, `proceedings.neurips.cc`.

Egulo **Candidate**. Venue quality Pending. DOI cell `Not Verified` thakle ota fill kora hoyni.

### PDF rule ja mana hoyeche

- Publisher OA / proceedings PDF / already-downloaded file copy
- HTML page ke PDF banano hoyni
- Paywall bypass hoyni
- Empty fake PDF banano hoyni

---

## 7. Screening register FINAL e ki

`02_SCREENING/Master_Literature_Database.xlsx`

- 158 row. Egulo identity-checked PDF + full-text label
- Eta 419 bibliography na. Bibliography POST e
- Status (ei file): Candidate 14, Pending 135, Excluded 9

`02_SCREENING/Exclusion_Register.xlsx`

- Oi 9. Reason: full-text suggestion Exclude, ba PDF missing/duplicate hash
- ArXiv-host Include suggestion ke exclusion list e dhukano hoyni. Ora Pending

`05_LITERATURE_ANALYSIS/Paper_Analysis_Matrix.xlsx`

- Sudhu 14 candidate
- Long cell = age full-text extraction er excerpt
- `Not Reported` = alada field chilo na. Title dekhe lekha hoyni
- `Agent_Type` jekhane threat-model excerpt er copy chilo, seta `Not Reported` kora hoyeche. Excerpt `Threat_Model` column e ache
- Venue quality: 14/14 Pending

---

## 8. Framework — ki, keno, kothay

Path: `06_PROPOSED_FRAMEWORK/`

Figure: `figures/AgentShield_LCE_workflow.png`

Dosh stage:

1. Identify agent, tools, assets
2. Map attack surfaces — gate G1
3. Define security requirements
4. Build paired test cases (benign + attack)
5. Run under instrumentation — gate G2
6. Score from traces — gate G3
7. Check detection coverage
8. Apply controls and retest — gate G4
9. Recover and reassess
10. Record a replayable report. Porer change Stage 2 te fire jay

Mitigation char class: prevent, detect, respond, recover. Attack success ekai report kora jabe na. Score trace er check e fire hobe, model er nijer boktobbo te na.

Keno 6-box sample diagram copy kora hoyni: oi sample onno stage name. Amader likha 10 stage + 4 gate.

Experiment validate kora hoyni. Ei kotha Framework_Design e ache.

---

## 9. Ja ja kora hoyni (defence e clear)

- Zotero library te record dhukano hoyni
- JCR / CiteScore quartile deya hoyni
- 50–70 final paper quota puron korte weak ba arXiv-only paper dhukano hoyni
- 18 ta IEEE PDF ke Top 30 rank e force-link kora hoyni
- Crossref 29 hit ke included study bola hoyni
- Historical phase er "Include suggestion" ke final inclusion bola hoyni
- Pirated PDF na

---

## 10. Ekhon obostha, ek line e

Bibliography ready: 419 exact-deduped records. PDF ready: 30 IEEE file + 14 proceedings file. Final venue-verified inclusion: **0**. Candidate: **14**. Framework design + figure ready. Baki: unmatched PDF identity check, legal publisher PDF, quartile evidence, tarpor Zotero import (add only, replace na).

---

## 11. Supervisor ke dekhale ei file gulo

1. `README.md` — count
2. `07_ZOTERO/POST/Deduplicated_Literature.xlsx` — bibliography
3. `07_ZOTERO/POST/Duplicate_Removal_Log.xlsx` — 15 duplicate
4. `02_SCREENING/IEEE_Top30_Register.xlsx` — 12 linked / 18 not linked
5. `03_SELECTED_LITERATURE/Final_Selected_Papers.xlsx` — 14 candidate, final na
6. `06_PROPOSED_FRAMEWORK/Framework_Design.md` + `figures/AgentShield_LCE_workflow.png`
7. `09_AUDIT/Validation_Report.md`
8. Original search log: IEEE workbook `Database_Search_Log`, Scholar workbook `Search_Log`
