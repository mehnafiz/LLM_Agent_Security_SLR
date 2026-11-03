# PRISMA-style flow

Counts are records, not “included studies.”

| Step | n | Rule |
|------|--:|------|
| IEEE paper table | 164 | `All_Collected_Papers` |
| Scholar paper table | 270 | `All_Related` |
| Identified before deduplication | 434 | PRE workbook |
| Removed as exact DOI or exact title duplicates | 15 | POST removal log |
| Unique bibliographic records | 419 | POST workbook |
| IEEE download PDFs retained | 30 | Pool folder, identity still per register |
| Publisher-host PDFs in Proceedings | see `03_SELECTED_LITERATURE/Final_Selected_Papers.xlsx` | Candidate until venue quality is verified |
| Eligible with venue quality verified | 0 | JCR/CiteScore not available; CORE A*/A not sufficient alone when the rest of the eligibility row is pending |

Records excluded for a reason are listed in `02_SCREENING/Exclusion_Register.xlsx` (full-text exclude or missing/duplicate PDF). Pending arXiv-hosted full texts are not in that exclusion register.
