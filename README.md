# LLM-Based Agent Security Evaluation

Systematic literature review workspace for attacks, evaluation metrics, mitigation, and framework design. The synthesis is **AgentShield-LCE**, a lifecycle for evaluating and improving the security of an LLM-based agent. It is a design. It has not been run as an experiment.

Original workbooks in the parent directory were not edited. Zotero was not modified. Import files are prepared only.

Consolidated 3 November 2026.

## Status

| Item | Count | Meaning |
|------|------:|---------|
| Records before duplicate removal | 434 | IEEE and Google Scholar tables stacked |
| Records after exact duplicate removal | 419 | Same DOI, or the same title when no DOI is present |
| Duplicates removed | 15 | The IEEE row was kept when both sources matched |
| IEEE PDFs on disk | 30 | One file each, directly in `04_FULL_TEXT_PDFS/IEEE/` |
| Top 30 ranks linked to a PDF | 12 | See the IEEE register. The other 18 ranks are marked **Not linked** |
| Proceedings candidates | 14 | Publisher-host PDF and a full-text Include suggestion |
| Papers with verified venue quality | 0 | Journal quartiles were not available |

Rank 12 of the IEEE Top 30 is excluded because the source title begins with `[Short Paper]`.

No DOI, venue, quartile, or abstract was filled in where the source record did not already contain it.

## Where to start

| If you need | Open |
|-------------|------|
| The research question and inclusion rules | `00_PROTOCOL/` |
| The bibliography before and after duplicate removal | `07_ZOTERO/PRE/` and `07_ZOTERO/POST/` |
| Which IEEE Top 30 paper has a PDF | `02_SCREENING/IEEE_Top30_Register.xlsx` |
| The 14 candidate papers | `03_SELECTED_LITERATURE/Final_Selected_Papers.xlsx` |
| The proposed lifecycle | `06_PROPOSED_FRAMEWORK/Framework_Design.md` |
| The workflow figure | `06_PROPOSED_FRAMEWORK/figures/AgentShield_LCE_workflow.png` |
| Counts, search, and screening notes | `08_REPORTS/` |
| File list and checksums | `09_AUDIT/` |

Each project workbook opens with a **How_To_Read** sheet.

## Folder guide

| Folder | Contents |
|--------|----------|
| `00_PROTOCOL/` | Objectives, eligibility criteria, and the review protocol |
| `01_SOURCE_DATABASES/` | Copies of the IEEE and Google Scholar workbooks, plus a Crossref metadata search |
| `02_SCREENING/` | Full-text register, IEEE Top 30 register, and the exclusion list |
| `03_SELECTED_LITERATURE/` | The 14 candidate papers. These are not final inclusions |
| `04_FULL_TEXT_PDFS/IEEE/` | The 30 downloaded IEEE-related PDFs |
| `04_FULL_TEXT_PDFS/Proceedings/` | The 14 proceedings PDFs |
| `05_LITERATURE_ANALYSIS/` | Analysis matrix for the 14 candidates, and the research-gap note |
| `06_PROPOSED_FRAMEWORK/` | AgentShield-LCE: stages, threat model, metrics, mitigation, and gates |
| `07_ZOTERO/` | PRE merge, POST deduplicated set, removal log, and a RIS file |
| `08_REPORTS/` | Search strategy, screening, venue quality, PRISMA-style counts, and the consolidation note |
| `09_AUDIT/` | Manifest, SHA-256 checksums, decision log, and validation |

## Bibliography files

| File | Rows | Rule |
|------|-----:|------|
| `07_ZOTERO/PRE/Merged_IEEE_and_Scholar.xlsx` | 434 | 434 actual paper rows with source, title, and full BibTeX; duplicates kept |
| `07_ZOTERO/POST/Deduplicated_Literature.xlsx` | 419 | 419 actual paper rows with source, title, and full BibTeX |
| `07_ZOTERO/POST/Duplicate_Removal_Log.xlsx` | 15 | 15 actual removed papers with full BibTeX and kept-match details |
| `07_ZOTERO/POST/Deduplicated_Literature.ris` | 419 | For a later manual Zotero import |

`07_ZOTERO/Zotero_Change_Log.md` records that these files were prepared and not imported.

## Framework

Read `06_PROPOSED_FRAMEWORK/Framework_Design.md` first. The figure is `figures/AgentShield_LCE_workflow.png`.

| File | Role |
|------|------|
| `Lifecycle_Architecture.md` | Stage order, inputs, outputs, and fail routes |
| `Threat_Model.md` | Assets, attackers, and the check that shows an attack succeeded |
| `Evaluation_Protocol.md` | Metrics, and the rule that a score must match a trace |
| `Mitigation_Strategy.md` | Prevent, detect, respond, and recover |
| `figures/stage_gates.md` | Gates G1–G4 |

## Open work

- Link the 18 unmatched Top 30 ranks to a PDF only after the file identity is checked, or obtain a legal publisher PDF.
- Add journal-quartile evidence before any candidate is marked finally included.
- Import the POST RIS into Zotero only as an addition to the existing library.
