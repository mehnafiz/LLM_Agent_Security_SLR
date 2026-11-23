# LLM-Based Agent Security Evaluation

Systematic literature review of the security of LLM-based agents. The review covers four dimensions: attack, evaluation metrics and benchmarks, mitigation, and proposed frameworks. Mitigation is the priority dimension.

`SLR_Record_Flow.xlsx` holds the stage counts. `SLR_Record_Flow.md` is the manuscript-ready write-up of the same flow. The folders below follow that order.

```
4,500 collected
  → 3,059 after duplicate removal
  → 606 kept after the quality split
  → 100 in the final set
  → 71 open full texts for analysis
```

The analysis corpus is always a single total: **N = 71**.

## Where to start

| Need | Open |
|---|---|
| Stage counts | `SLR_Record_Flow.xlsx` |
| Selection narrative (Q1-ready) | `SLR_Record_Flow.md` |
| PRISMA flow figure | `PRISMA_Flow.png` |
| Inclusion / exclusion criteria (Table 2) | `04_Screening/Inclusion_Exclusion_Criteria.xlsx` |
| The 100 final papers | `04_Screening/Final_Relevant_Literature.xlsx` |
| Why a paper was kept or left out | `04_Screening/Title_Abstract_Screening_and_PDF_Retrieval_Report.md` |
| PDF status for the 100 | `05_Full_Texts/Final_PDF_Verification.xlsx` |
| Full-text summaries of the 71 papers | `05_Full_Texts/Paper_Summaries_71.xlsx` |
| Framework comparison (AgentShield-LCE first) | `06_Framework/Framework_Comparison.xlsx` |
| Shared systems across papers | `06_Framework/Shared_Frameworks_Across_Papers.xlsx` |
| Testbed / AS compatibility fields | `06_Framework/Testbed_and_Compatibility_Comparison.xlsx` |
| Upgraded literature analysis pack | `05_LITERATURE_ANALYSIS/` |
| Proposed framework design | `06_Framework/Framework_Design.md` |
| Full methodology write-up | `Research_Methodology.pdf` (source: `Research_Methodology.md`) |

## Record flow

| Stage | Folder | Result |
|---|---|---|
| Collection | `01_Collection` | 4,500 records, before duplicate removal |
| Deduplication | `02_Deduplication` | 1,441 duplicate records removed; 3,059 unique papers remain |
| Quality split | `03_Quality` | 606 kept for screening; 2,453 set aside |
| Screening | `04_Screening` | 100 in the final set; 506 not in that set |
| Full text | `05_Full_Texts` | 71 open full texts for analysis; 29 selected papers retained but not full-text coded |
| Framework | `06_Framework` | AgentShield-LCE design notes, figures, comparison, shared-systems, and testbed-compatibility workbooks |
| Literature analysis (upgraded) | `05_LITERATURE_ANALYSIS` | Upgraded comparison, shared-systems, evidence register, and claims workbooks |

The quality split had an earlier pass of 486 kept and 2,573 set aside. A CORE rank check then moved 120 records into the kept set, which is the 606 used for screening.

Of the 506 papers outside the final set: 193 were excluded on the title, 141 on the abstract, 36 had no abstract and were not scored, 4 were uncertain, and 132 were relevant but ranked outside the top 100.

Of the 100 relevance-ranked papers, 71 provided a title-verified full text under open retrieval conditions and were included in full-text analysis (`Downloaded_Verified` 44 + `Preprint_Verified` 27). The remaining 29 selected papers were retained in the inventory but excluded from full-text coding because a lawful open full text was not available at analysis time (`Paywalled` 28 + `Access_Denied` 1). Details are in `SLR_Record_Flow.md` and `PRISMA_Flow.png`.

## Files

**01_Collection**

- `Before_Duplicate_Removal.xlsx` — every collected row, 4,500. Sheet `Collected_4500`. Of these, 3,059 are unique papers and 1,441 are exact duplicate copies of those papers. Paper IDs stop at `P003061` because the duplicate copies reuse the same ID.

**02_Deduplication**

- `After_Duplicate_Removal.xlsx` — 3,059 unique papers. Sheet `Unique_3059`. This is the file used for the quality split.
- `Duplicate_Removal_Count.xlsx` — 4,500 before removal, 3,059 after.

The Zotero export of this stage was not kept. It repeated two IDs, omitted `P000873` and `P002352`, and replaced `P000818` with a Zotero key. The before-removal Zotero workbook was a byte-identical copy of `Before_Duplicate_Removal.xlsx`, so that copy was not kept either.

**03_Quality**

- `Selected_Quality_Literature.xlsx` — 606 papers screened in the next stage.
- `Excluded_Lower_Quality_Literature.xlsx` — 2,453 papers set aside.
- `evidence/` — the quality-filtering report, the cross-verification report, the ICORE 2026 rank list, and the Crossref cache.
- `backups/2026-11-07_pre_crosscheck/` — the two workbooks as they stood before the rank check.

**04_Screening**

- `Final_Relevant_Literature.xlsx` — the final 100, ranked by relevance score. The highest score is 83 and the lowest in this set is 62.
- `Screening_Reserve_and_Excluded.xlsx` — the other 506 records from the selected-quality set.
- `Inclusion_Exclusion_Criteria.xlsx` — Table 2 inclusion/exclusion criteria (also `.md` / `.png`).
- `Title_Abstract_Screening_and_PDF_Retrieval_Report.md` — screening method, dimension counts, and PDF outcomes.

Scores use the title and abstract only: direct relevance (30), attack (15), evaluation (15), mitigation (20), framework (15), and practical usefulness (5). Venue rank is not part of the score.

**05_Full_Texts**

PDFs are grouped by filing folder: `Attack` (16), `Evaluation_Benchmarks` (7), `Mitigation` (9), `Framework` (1), and `Multi_Dimensional` (38). Total open PDFs = **71**. A paper is filed under `Multi_Dimensional` when at least two components are strong.

- `Final_PDF_Verification.xlsx` — status and path for each of the 100 selected papers.
- `Paper_Summaries_71.xlsx` — BibTeX, abstract, contribution/result, limitations, critics for each open full text.
- `PRISMA_Flow.png` / `.svg` — copies of the flow figure.

**05_LITERATURE_ANALYSIS**

Upgraded literature-analysis pack (keeps new deep-analysis outputs in one place):

- `Framework_Comparison_Upgraded.xlsx` — fair comparison + capability matrices
- `Shared_Frameworks_Across_Papers_Upgraded.xlsx` — shared systems with roles/page evidence
- `Paper_Evidence_Register.xlsx` — paper-level evidence register
- `Comparative_Claims_Register.xlsx` — comparative claims (draft; needs human spot-check)
- `AgentShield_Novelty_and_Positioning.md` / `Research_Gap_Analysis.md`

**06_Framework**

AgentShield-LCE is a proposed evaluation lifecycle. It is a design. It has not been run as an experiment.

| File | Contents |
|---|---|
| `Framework_Comparison.xlsx` | AgentShield-LCE first, then all 71 papers; sheets: Framework_Comparison, Not_In_Full_Text (29), Notes |
| `Shared_Frameworks_Across_Papers.xlsx` | Shared ecosystems/benchmarks across papers vs unique named contributions |
| `Testbed_and_Compatibility_Comparison.xlsx` | Testbed/model/tools/memory/attack/reproducibility + AgentShield-LCE compatibility mapping |
| `Framework_Design.md` | The design, compact literature snapshot, and limitations |
| `Lifecycle_Architecture.md` | The agent loop, stages 1–10, gates, components, and harness guidance |
| `Architecture_Components.md` | Component names. It does not add a stage beyond the lifecycle file |
| `Threat_Model.md` | Actors, assets, TB1–TB5, and surfaces |
| `Evaluation_Protocol.md` | Run manifest, ordered trace, detector fields, and metric denominators |
| `Mitigation_Strategy.md` | C1–C10, classes, evidence, and limits |
| `Figure_Captions.md` | Captions for the six figures |
| `figures/` | The six final figures. SVG is the source. PNG and PDF are exports. `build_figures.py` regenerates the SVG files |

## Scope of this workspace

The final 100 papers are the relevance-ranked set from title and abstract screening. An open PDF was retrieved only when a public copy was available. Paywalled papers were not downloaded. Full-text coding and framework comparison use the **71** open PDFs only.
