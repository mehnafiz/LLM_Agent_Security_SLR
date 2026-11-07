# Publication-quality filtering

Date: 2026-11-07. Classification only. No original workbook, PDF, or framework file was edited.

## Which file was classified

`02_SCREENING/Master_Literature_Database.xlsx` is the full-text screening register (158 paper rows). It is not the bibliography.

The classified file is the deduplicated bibliography:

`02_Deduplication/After_Duplicate_Removal.xlsx`

It has 3,059 data rows and 3,059 distinct `Paper_ID` values. The undeduplicated collection is `01_Collection/Before_Duplicate_Removal.xlsx`, which has 4,500 data rows and was not reopened into the outputs.

A Zotero export of the same stage also had 3,059 rows, but only 3,057 distinct IDs. It repeated `P000231` and `P000685`, omitted `P000873` and `P002352`, and replaced `P000818` with Zotero key `Z-9XY6VHXI` for DOI `10.48550/arxiv.2504.00218`. That export was not kept. This workbook keeps the three omitted or relabeled records under their original IDs.

## What was and was not verified

| Source | Result |
|---|---|
| Crossref works API | Retrieved for 1,134 DOIs: work type, publisher, container title, ISSN when Crossref provided one. Evidence URL is the Crossref work URL. Cache: `03_Quality/evidence/crossref_work_metadata.jsonl` |
| DOI absent | 952 records |
| DOI not in Crossref | 973 records. A random sample of 12, and 15 further scholarly-looking DOIs, returned HTTP 404 on single-record lookup. Most are `10.48550/arxiv` |
| JCR | Not accessed. No JCR quartile was assigned |
| Scopus CiteScore | Not accessed. No CiteScore quartile was assigned |
| CORE / CCF | The CORE export URL returned 404, and no CCF list was retrieved. No CORE or CCF rank was assigned |
| OpenAlex | Rate-limited (HTTP 429). Not used |

A blank rank is not a low rank. Categories 1–11 and 13 are empty because the evidence those categories require was not available. That is not a finding that the corpus contains no Q1 journals.

## Counts

These figures are the first pass. The workbooks were updated afterward: the cross-verification report records the current counts, 606 kept and 2,453 set aside.

`3,059 = 486 selected + 2,573 excluded`

| Check | Result |
|---|---:|
| Source records | 3059 |
| Selected | 486 |
| Excluded | 2573 |
| Missing from both | 0 |
| Present in both | 0 |
| Exact duplicate DOIs inside the source | 0 |

Selected file: `03_Quality/Selected_Quality_Literature.xlsx`, sheet `Selected_Papers`. Header frozen, filter on.

Excluded file: `03_Quality/Excluded_Lower_Quality_Literature.xlsx`, sheet `Excluded_Papers`. Header frozen, filter on.

Both were reopened. Selected rows are ordered by priority 12, then publication year descending, then title.

## Selected records

Every selected record is priority 12, category “Other peer-reviewed conferences and workshops”, level “Lower”. No record was placed in priorities 1–11 or 13.

| Group | Records |
|---|---:|
| IEEE conference proceedings, category 12, CORE/CCF not verified | 307 |
| Other proceedings from ACL, ACM, Springer, AAAI, NeurIPS, USENIX, Internet Society, PMLR, or Elsevier, with a conference or workshop container title | 179 |
| Of the 486, workshop papers (container title contains “workshop”) | 55 |
| Conference papers | 431 |
| IEEE journals retained | 0 |
| Records with a verified JCR, Scopus, CORE, or CCF rank | 0 |

IEEE retention used here: Crossref type `proceedings-article`, an IEEE DOI or publisher, a container title, and a title that is not a short paper, poster, or demo. That is category 12. It is not a claim that the conference is CORE A or CCF A.

## Excluded records

| Group | Records |
|---|---:|
| Preprint or repository posting only | 1863 |
| Journal article; quartile and indexing not verified | 334 |
| Proceedings container title is not a conference or workshop volume | 112 |
| Proceedings publisher not verified for category 12 | 11 |
| Short paper, poster, or demo | 3 |
| Book chapter | 64 |
| Book | 6 |
| Monograph | 3 |
| Dissertation | 2 |
| Report or report component | 3 |
| Review or peer-review record | 2 |
| IEEE record whose journal-versus-conference type was not returned | 9 |
| Venue not verified | 161 |

IEEE items inside the excluded file:

| IEEE status | Records | Why excluded |
|---|---:|---|
| IEEE journal | 58 | JCR and Scopus were not accessible, so categories 1, 3, 5, 6, 8, 10, and 11 were not assigned |
| IEEE conference proceedings | 3 | Title is a poster or a short paper |
| IEEE record, type not verified | 19 | IEEE name or URL present, but Crossref did not return a work type |

## Duplicates

No source DOI is repeated. Three title strings collide after punctuation is removed. They were not merged, and none is split across the two workbooks:

- “Jailbreaking and Mitigation of Vulnerabilities in Large Language Models”: `P000185` (OSF preprint, 2024) and `P001923` (journal DOI, 2026). Both excluded.
- “Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems”: `P000685` (2025, preprint DOI) and `P002352` (2026, Springer book-chapter DOI). Both excluded. The chapter was not treated as the same record as the preprint.
- “Prompt Injection” against the Cyrillic title of `P000873` after non-Latin letters were stripped. That collision is an artifact of normalization, not a duplicate decision.

## Unresolved

- Journal quartiles, Scopus indexing, and CORE/CCF ranks remain unresolved for every record.
- 58 IEEE journals stay in the excluded workbook until a JCR or Scopus source is actually opened.
- 179 non-IEEE proceedings are category 12 because Crossref names a proceedings volume from a publisher that issues peer-reviewed proceedings. That is not a CORE rank.
- 112 proceedings-articles were left out because the container title does not name a conference or workshop. Some of those venues may still be legitimate. They were not upgraded by guesswork.
