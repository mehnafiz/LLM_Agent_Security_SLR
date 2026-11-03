# Search strategy

## Already executed (source workbooks, not re-typed here)

The IEEE workbook sheet `Database_Search_Log` stores the IEEE queries, dates, fields, filters, and result counts. The Scholar workbook sheet `Search_Log` stores the Scholar queries, year filter, and pages saved. Those sheets are inside:

- `01_SOURCE_DATABASES/IEEE/IEEE_Source_Collection.xlsx`
- `01_SOURCE_DATABASES/Google_Scholar/Google_Scholar_Source_Collection.xlsx`

They are copies. The originals in the parent directory were not modified.

## Recorded coverage

| Source | Paper-table rows | Deduplicated role |
|--------|-----------------:|-------------------|
| IEEE `All_Collected_Papers` | 164 | Bibliographic master when a DOI or title collides |
| Google Scholar `All_Related` | 270 | Discovery source; dropped when an exact DOI or title match exists |
| PRE stack | 434 | `07_ZOTERO/PRE/Merged_IEEE_and_Scholar.xlsx` |
| POST unique | 419 | `07_ZOTERO/POST/Deduplicated_Literature.xlsx` |

## Supplementary metadata search

`01_SOURCE_DATABASES/Other_Databases/Supplementary_Crossref_Search.xlsx` lists Crossref hits from 2026-11-03. A hit is a candidate title and DOI. It is not an included study until it passes the eligibility fields.

## What was not searched in this consolidation

Clarivate JCR and Scopus CiteScore were not queried (no licensed session). No paywalled PDF was downloaded.
