# Final consolidation note (2026-11-03)

## Question

How should the security of an LLM-based agent be evaluated across attacks, metrics, mitigations, and framework design, with mitigation treated as a lifecycle control rather than a single add-on?

## Corpus actually in this folder

- 434 source rows merged from the two workbooks (PRE).
- 419 rows after exact duplicate removal (POST).
- 30 IEEE-related PDFs copied from the download directory.
- Publisher-proceedings PDFs for the candidate set listed in `Final_Selected_Papers.xlsx`.
- Analysis matrix filled from the full-text extraction fields that exist; missing fields stay `Not Reported`.

## Synthesis

AgentShield-LCE (see `06_PROPOSED_FRAMEWORK/`) requires paired benign and attack tests, oracles on traces, four control classes, and four gates. It is a design. No experiment in this repository validates it.

## Limitations

- Licensed journal metrics were not available, so venue quality is pending for almost every row.
- Most identity-checked PDFs from the earlier retrieval are arXiv copies and are not eligible.
- Eighteen IEEE download files are in the pool but not auto-assigned to a Top 30 rank, because the folder prefix is not the rank and the PDF text did not confirm the title.
- Zotero was not updated. Import the POST RIS only after a person checks it.

## Next actions

1. Manually link the unmatched IEEE PDFs using `Download_Pool_Index`.
2. Replace arXiv PDFs with publisher open copies where one exists.
3. Add JCR or CiteScore evidence before any row is marked venue-verified.
4. Import `07_ZOTERO/POST/Deduplicated_Literature.ris` only as an addition. Do not replace an existing Zotero library.
