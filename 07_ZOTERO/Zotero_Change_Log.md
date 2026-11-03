# Zotero change log (2026-11-03)

## Application

Zotero was not opened and no library was modified.

## PRE

`PRE/Merged_IEEE_and_Scholar.xlsx` stacks the IEEE `All_Collected_Papers` sheet (164 rows) and the Google Scholar `All_Related` sheet (270 rows). Total 434. Both copies of a duplicate are present.

## POST

`POST/Deduplicated_Literature.xlsx` has 419 rows.

Removal rule: same DOI, otherwise the same normalized title. The IEEE row is kept when both sources match. 15 rows are listed in `POST/Duplicate_Removal_Log.xlsx` and are absent from the unique sheet.

`POST/Deduplicated_Literature.ris` is an import file for a person to add later. Importing it is not part of this log.

## Not done

- No existing Zotero collection was deleted or overwritten.
- PRE is not a Zotero export of a live library. It is the merge of the two project workbooks.
