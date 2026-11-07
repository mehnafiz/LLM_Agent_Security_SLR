# LLM-Based Agent Security Evaluation

Systematic literature review of the security of LLM-based agents. The review covers four dimensions: attack, evaluation metrics and benchmarks, mitigation, and proposed frameworks. Mitigation is the priority dimension.

`SLR_Record_Flow.xlsx` is the count for every stage. The folders below follow that same order.

```
4,500 collected
  → 3,059 after duplicate removal
  → 606 kept after the quality split
  → 100 in the final set
  → 68 open PDFs
```

## Where to start

| Need | Open |
|---|---|
| Stage counts | `SLR_Record_Flow.xlsx` |
| The 100 final papers | `04_Screening/Final_Relevant_Literature.xlsx` |
| Why a paper was kept or left out | `04_Screening/Title_Abstract_Screening_and_PDF_Retrieval_Report.md` |
| An open PDF | `05_Full_Texts/`, then `Final_PDF_Verification.xlsx` for the path and status |
| The proposed lifecycle | `06_Framework/Framework_Design.md` |

## Record flow

| Stage | Folder | Result |
|---|---|---|
| Collection | `01_Collection` | 4,500 records, before duplicate removal |
| Deduplication | `02_Deduplication` | 1,441 duplicate records removed; 3,059 unique papers remain |
| Quality split | `03_Quality` | 606 kept for screening; 2,453 set aside |
| Screening | `04_Screening` | 100 in the final set; 506 not in that set |
| Full text | `05_Full_Texts` | 68 open PDFs retrieved; 31 paywalled; 1 access denied |
| Framework | `06_Framework` | AgentShield-LCE design notes and figures |

The quality split had an earlier pass of 486 kept and 2,573 set aside. A CORE rank check then moved 120 records into the kept set, which is the 606 used for screening.

Of the 506 papers outside the final set: 193 were excluded on the title, 141 on the abstract, 36 had no abstract and were not scored, 4 were uncertain, and 132 were relevant but ranked outside the top 100.

Of the 68 PDFs: 41 are official proceedings copies and 27 are verified arXiv preprints. The preprints are labeled as preprints.

## Files

**01_Collection**

- `RAW_LITERATURE_DATABASE.xlsx` — the collected bibliography, 4,500 rows.

**02_Deduplication**

- `RAW_LITERATURE_DATABASE_SORTED.xlsx` — 3,059 unique papers. This is the file used for the quality split.
- `Zotero_After_Duplicate_Removal.xlsx` — the Zotero export of the same stage. It has 3,059 rows and 3,057 distinct IDs.
- `Duplicate_Removal_Count.xlsx` — 4,500 before removal, 3,059 after.

The Zotero before-removal workbook was a byte-identical copy of the raw collection, so one copy is kept.

**03_Quality**

- `Selected_Quality_Literature.xlsx` — 606 papers screened in the next stage.
- `Excluded_Lower_Quality_Literature.xlsx` — 2,453 papers set aside.
- `evidence/` — the quality-filtering report, the cross-verification report, the ICORE 2026 rank list, and the Crossref cache.
- `backups/2026-11-07_pre_crosscheck/` — the two workbooks as they stood before the rank check.

**04_Screening**

- `Final_Relevant_Literature.xlsx` — the final 100, ranked by relevance score. The highest score is 83 and the lowest in this set is 62.
- `Screening_Reserve_and_Excluded.xlsx` — the other 506 records from the selected-quality set.
- `Title_Abstract_Screening_and_PDF_Retrieval_Report.md` — screening method, dimension counts, and PDF outcomes.

Scores use the title and abstract only: direct relevance (30), attack (15), evaluation (15), mitigation (20), framework (15), and practical usefulness (5). Venue rank is not part of the score.

**05_Full_Texts**

PDFs are grouped by the dimension used for filing: `Attack`, `Evaluation_Benchmarks`, `Mitigation`, `Framework`, and `Multi_Dimensional`. A paper is filed under `Multi_Dimensional` when at least two components are strong.

`Final_PDF_Verification.xlsx` records the status, version, and local path for each of the 100 final papers. A file was kept only when it opened as a PDF and the title matched the selected record.

**06_Framework**

AgentShield-LCE is a proposed evaluation lifecycle. It is a design. It has not been run as an experiment.

| File | Contents |
|---|---|
| `Framework_Design.md` | The design and what it does not claim as a new benchmark |
| `Lifecycle_Architecture.md` | Stage order, inputs, outputs, and fail routes |
| `Threat_Model.md` | Assets, attackers, and the check that an attack succeeded |
| `Evaluation_Protocol.md` | Metrics, and the rule that a score must match a trace |
| `Mitigation_Strategy.md` | Prevent, detect, respond, and recover |
| `figures/` | Figures 1–6, as PNG and SVG |
| `figures/stage_gates.md` | Gates G1–G4 |

## Scope of this workspace

The final 100 papers are the relevance-ranked set from title and abstract screening. An open PDF was retrieved only when a public copy was available. Paywalled papers were not downloaded.
