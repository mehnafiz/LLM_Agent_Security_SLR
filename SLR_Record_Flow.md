# Study Selection and Record Flow

This note accompanies `SLR_Record_Flow.xlsx` and `PRISMA_Flow.png`. It explains, in manuscript-ready form, how records were retained or set aside, how relevance was scored, why the final analysis set is smaller than the screened set, and how full-text availability was handled.

## 1. Overview

The review began with **4,500** bibliographic records and ended with **71** full texts used for deep analysis. The reduction is the product of four deliberate filters:

1. exact-duplicate removal;
2. publication-quality prioritization;
3. title/abstract relevance ranking for LLM-agent security;
4. full-text inclusion restricted to title-verified, openly retrievable PDFs.

The **selected relevance set remains 100 papers**. The **full-text analysis set is 71 papers**. Papers without an open full text were not deleted from the study; they remain documented as selected-but-not-coded pending lawful full-text access.

## 2. Identification

| Stage | Count | Meaning |
|---|---:|---|
| Records identified from the database | 4,500 | Raw collection before cleaning |
| Exact duplicate records removed | 1,441 | Same paper ID / identical bibliographic copies |
| Unique records retained | 3,059 | Input to quality filtering |

Duplicates were removed before any relevance judgment so that later scores would not reward repeated copies of the same work.

## 3. Quality filtering

Unique records were split by publication-quality rules used in this project (venue rank / indexing evidence), then adjusted by a CORE-rank cross-check:

| Item | Count |
|---|---:|
| First quality pass kept | 486 |
| First quality pass set aside | 2,573 |
| Moved into the kept set after CORE rank check | 120 |
| Final kept for screening | **606** |
| Final set aside as lower quality | **2,453** |

Records set aside at this stage were not judged irrelevant to agent security; they were deprioritized on the project’s quality criteria so that screening effort concentrated on the higher-priority subset.

## 4. Title and abstract screening

Formal inclusion and exclusion criteria are in `04_Screening/Inclusion_Exclusion_Criteria.xlsx` (manuscript sheet + notes on arXiv/archives; also `.md` / `.png`).

All **606** quality-selected records received title screening. Records not excluded on title were then judged from the stored abstract.

### 4.1 Exclusion and retention logic

A title was excluded only when it was clearly outside the security of LLM-based agents (for example, generic chatbot jailbreaks with no tool/memory/agent action, non-security agent applications, or papers that use agents only as offensive tools against unrelated software).

Abstracts were scored only when a usable abstract existed. Missing abstracts were not given a fabricated score.

### 4.2 Relevance score (basis for top vs low)

Scores used **title and abstract evidence only**, with fixed weights:

| Component | Max points | Role |
|---|---:|---|
| Direct relevance to LLM-agent security | 30 | Must be about agents that act (tools, memory, multi-agent, etc.) |
| Attack | 15 | Threat/red-team contribution |
| Evaluation / benchmarks | 15 | Measurement contribution |
| Mitigation | 20 | Defense contribution (priority dimension) |
| Framework | 15 | Architecture / protocol contribution |
| Practical usefulness | 5 | Deployability / realism signal |
| **Total** | **100** | |

Venue prestige was **not** part of the score. Venue/quality priority was used only as a later tie-breaker.

Ranking order:

1. relevance score (descending);
2. directness of agent-security focus;
3. original quality priority;
4. year.

### 4.3 Outcomes from 606 records

| Outcome | Count | Interpretation |
|---|---:|---|
| Final selected set | **100** | Highest-ranked includable papers (scores 83 down to 62) |
| Excluded at title | 193 | Outside scope on title |
| Excluded at abstract | 141 | Outside scope after abstract reading |
| No abstract, not scored | 36 | Could not be ranked fairly |
| Uncertain | 4 | Insufficient evidence to include in the top set |
| Relevant but outside top 100 (reserve) | 132 | Includable, retained as reserve, not in the primary 100 |
| **Not in final set (sum)** | **506** | 193+141+36+4+132 |

The primary set is the **top 100**, not “all papers above an arbitrary low cutoff.” More than 100 records were plausible includes; the project fixed a transparent ranked primary set and kept the remainder as reserve.

## 5. Full-text inclusion (why 100 became 71)

Full-text coding requires a **reproducible local PDF** whose extracted text or metadata matches the selected title. Retrieval used open locations only (for example ACL Anthology, NDSS DOI pages, AAAI proceedings, and verified arXiv preprints). Subscription barriers were not bypassed.

| Outcome | Count |
|---|---:|
| Final selected papers | 100 |
| **Studies included in full-text analysis** | **71** |
| Selected papers without open full text | **29** |
| — no open PDF under retrieval conditions | 28 |
| — open location access denied | 1 |

The analysis corpus is always reported as a single total (**N = 71**). Figures and main text do not split that total into retrieval-pass subcounts.

### 5.1 How this is reported (recommended manuscript language)

Use wording of this form:

> Of the 100 relevance-ranked papers, 71 provided a title-verified full text under open retrieval conditions and were included in the full-text analysis. The remaining 29 selected papers were retained in the study inventory but excluded from full-text coding because a lawful open full text was not available at the time of analysis. This criterion preserves reproducibility of the coded evidence base; it is an access constraint on full-text coding, not a second relevance ranking.

Avoid weak phrasing such as “we could not download the papers.” Prefer:

- “full text not available under open-access retrieval conditions”;
- “retained in the selected set; excluded from full-text coding pending access”;
- “analysis corpus = openly verifiable full texts.”

### 5.2 What this does and does not mean

- It does **not** mean the 29 papers are irrelevant.
- It does **not** mean the 71 papers are the “best 71 by quality.”
- It **does** mean claims that depend on section-level evidence (methods, metrics, limitations, architecture) are grounded only in PDFs that can be reopened and rechecked.

The 29 non-coded selected titles are listed in `05_Full_Texts/Final_PDF_Verification.xlsx` and in `Framework_Comparison.xlsx` (sheet `Not_In_Full_Text`).

## 6. Organization of the 71 full texts

PDFs are filed by research dimension:

| Folder | Role |
|---|---|
| `Attack/` | Primarily attack / red-teaming |
| `Evaluation_Benchmarks/` | Primarily benchmarks or evaluation studies |
| `Mitigation/` | Primarily defenses |
| `Framework/` | Primarily frameworks/architectures |
| `Multi_Dimensional/` | At least two strong dimensions |

## 7. Implications for AgentShield-LCE positioning

Comparative claims about AgentShield-LCE use only:

1. the current design documents in `06_Framework/`; and
2. full texts among the 71 open PDFs.

Where an existing system is experimentally validated and AgentShield-LCE is not, that experimental strength is acknowledged. AgentShield-LCE’s defensible advantage is evaluation-governance coverage (stages, gates, denominators, leftovers, reassessment, recovery, release record), not an unmeasured performance ranking.

## 8. Source files

- Stage counts: `SLR_Record_Flow.xlsx`
- Full methodology: `Research_Methodology.pdf`
- Flow figure: `PRISMA_Flow.png`
- Inclusion/exclusion criteria: `04_Screening/Inclusion_Exclusion_Criteria.xlsx`
- Selected 100: `04_Screening/Final_Relevant_Literature.xlsx`
- Reserve/excluded 506: `04_Screening/Screening_Reserve_and_Excluded.xlsx`
- PDF status: `05_Full_Texts/Final_PDF_Verification.xlsx`
- Full-text summaries (71): `05_Full_Texts/Paper_Summaries_71.xlsx`
- Framework comparison (AgentShield-LCE + 71): `06_Framework/Framework_Comparison.xlsx`
