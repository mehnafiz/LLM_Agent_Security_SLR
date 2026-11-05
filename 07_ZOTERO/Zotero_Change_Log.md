# Zotero bibliography preparation log (2026-11-05)

## Workbook contents

All three XLSX files are paper-record tables. The first row is the column header; the rows below it contain actual records. There are no summary or instruction sheets in these workbooks.

- `PRE/Merged_IEEE_and_Scholar.xlsx`: 434 paper records (164 IEEE + 270 Google Scholar), with `Record_ID`, `Source`, `Title`, and the source workbook's full `BibTeX` entry. Both sides of duplicates remain.
- `POST/Deduplicated_Literature.xlsx`: 419 retained paper records, with the same four columns and each retained record's full source BibTeX.
- `POST/Duplicate_Removal_Log.xlsx`: 15 removed duplicate paper records. Each row contains the removed paper's title and full BibTeX, plus the kept record's ID/title and the match key/reason.

Deduplication follows the existing decision crosswalk: exact DOI when available, otherwise normalized title; IEEE is retained when both sources match.

## Application status

Zotero was not opened and no live library was modified. `POST/Deduplicated_Literature.ris` remains available for a later manual import; importing it was not performed here.
