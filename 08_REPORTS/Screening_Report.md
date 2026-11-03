# Screening report

## What is decided in this folder

- Bibliographic identity after exact DOI / exact title merge: see POST.
- PDF presence for the IEEE downloads: 30 files directly under `04_FULL_TEXT_PDFS/IEEE/`.
- Rank-to-file link for the IEEE Top 30: only the rows in `02_SCREENING/IEEE_Top30_Register.xlsx` whose match method is filled. Unmatched ranks stay unmatched.
- Publisher-host PDFs copied into `04_FULL_TEXT_PDFS/Proceedings/` are candidates, not venue-verified inclusions.

## What is not re-decided here

Historical IEEE screening (include / review / exclude), title screening, abstract screening, and full-text suggestions remain in `LLM_Agent_Security_SLR/`. They are not copied back into this folder as a second screening log, because that copy was being mistaken for a new phase.

A full-text “Include” suggestion does not override an arXiv PDF. Those rows stay pending in `02_SCREENING/Master_Literature_Database.xlsx`.
