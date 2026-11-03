# LLM Agent Security — Final SLR Project

Clean final workspace (not phase-based). Original data stays in parent folders unchanged.

## Layout
| Folder | Contents |
|--------|----------|
| `00_PROTOCOL/` | Objectives, eligibility, protocol |
| `01_SOURCE_DATABASES/` | IEEE + Scholar workbook copies; Crossref supplement |
| `02_SCREENING/` | Master register, **IEEE Top 30 register**, exclusions |
| `03_SELECTED_LITERATURE/` | Publisher-version selected papers |
| `04_FULL_TEXT_PDFS/IEEE/` | One PDF per downloaded paper. No subfolder. |
| `04_FULL_TEXT_PDFS/Proceedings/` | Non-IEEE publisher PDFs (full-text corpus subset) |
| `05_LITERATURE_ANALYSIS/` | Analysis matrix + research gaps |
| `06_PROPOSED_FRAMEWORK/` | AgentShield-LCE draft |
| `07_ZOTERO/` | Import files only (Zotero not modified) |
| `08_REPORTS/` | PRISMA, search, screening summary |
| `09_AUDIT/` | Checksums, manifest, validation |

## Counts (2026-11-03)
| Metric | Value |
|--------|------:|
| Bibliographic rows before duplicate removal (PRE) | 434 |
| Bibliographic rows after exact DOI or title removal (POST) | 419 |
| Exact duplicates removed | 15 |
| IEEE PDFs in `04_FULL_TEXT_PDFS/IEEE/` | 30 |
| Top 30 ranks with a PDF actually linked | 12 |
| Top 30 ranks with no linked PDF | 18 |
| Proceedings PDFs kept as candidates | 14 |
| Final inclusions with verified venue quality | 0 |

## What a full check found

Nothing required was invented to fill a gap.

- The two source workbooks are present as copies. They were not edited.
- PRE and POST are the merged bibliography. POST is the duplicate-removed set. Zotero itself was not changed.
- The IEEE folder has 30 PDFs and no inner folder. Only 12 of the Top 30 ranks are tied to a file. The other 18 files stay in the folder and are marked **Not linked** in `02_SCREENING/IEEE_Top30_Register.xlsx`.
- Rank 12 is excluded because its title begins with `[Short Paper]`.
- The 14 proceedings papers are candidates. Their DOI and venue are **Not Verified** in the project master, so those cells were left that way.
- Crossref rows are labeled metadata hits, not included studies.
- Audit files `File_Manifest.csv` and `SHA256_Checksums.csv` are real CSV files. An earlier version had an Excel file saved under a `.csv` name.
- Workbooks now have a `How_To_Read` sheet, a frozen header, and filters. Long cells wrap. Values were not rewritten except the corrections named in `09_AUDIT/Validation_Report.md`.

## Still open

Venue quartiles were not available, so no paper is marked finally included. Eighteen Top 30 ranks still need a human link to a PDF, or a legally downloaded publisher PDF.

## IEEE PDFs

All 30 downloaded PDFs sit directly in `04_FULL_TEXT_PDFS/IEEE/`. There is no inner folder and no second copy. Rank links are in `02_SCREENING/IEEE_Top30_Register.xlsx`.

## Zotero snapshots (application not modified)

| Path | Content |
|------|---------|
| `07_ZOTERO/PRE/Merged_IEEE_and_Scholar.xlsx` | 434 rows: IEEE paper table stacked with the Scholar paper table. Duplicates kept. |
| `07_ZOTERO/POST/Deduplicated_Literature.xlsx` | 419 rows after exact DOI or exact title collapse. IEEE row kept when both exist. |
| `07_ZOTERO/POST/Duplicate_Removal_Log.xlsx` | 15 removed rows and the canonical row they matched. |
| `07_ZOTERO/POST/Deduplicated_Literature.ris` | RIS for the POST rows, for a later manual import. |
| `07_ZOTERO/Zotero_Change_Log.md` | What was prepared and what was not imported. |

## Framework

Start at `06_PROPOSED_FRAMEWORK/Framework_Design.md` (one table of the ten stages). Then:

| File | What it answers |
|------|-----------------|
| `Lifecycle_Architecture.md` | Order, inputs, outputs, and where a failed gate sends you back |
| `Threat_Model.md` | Assets, attackers, and the check that proves an attack |
| `Evaluation_Protocol.md` | Which numbers to report, and the rule that a score must match a trace |
| `Mitigation_Strategy.md` | Prevent, detect, respond, and recover |
| `figures/stage_gates.md` | Gates G1–G4 |

This is a design, not an experiment.
