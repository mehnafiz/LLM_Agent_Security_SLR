# Title and abstract screening, relevance ranking, and full-text retrieval

Project: LLM-Based Agent Security Evaluation.

Source workbook, left unchanged during screening: `03_Quality/Selected_Quality_Literature.xlsx` (sheet `Selected_Papers`).

Screening outputs:

- `04_Screening/Final_Relevant_Literature.xlsx` (sheet `Final_Selected_Papers`)
- `04_Screening/Screening_Reserve_and_Excluded.xlsx` (sheet `Screening_Register`)
- `05_Full_Texts/`
- `05_Full_Texts/Final_PDF_Verification.xlsx`

The excluded-quality workbook and the raw collection were not modified during screening.

## How screening was done

Every title in the selected workbook was read. A title was excluded only when it was clearly outside the security of LLM-based agents: general jailbreaks of chat models, non-security agent applications, or papers that use agents only as tools against other software.

Every record that was not excluded on the title was then judged from the stored abstract. Papers with no usable abstract were marked `Abstract_Missing` and were not given a relevance score. Scores use only what the abstract supports: direct relevance to LLM-agent security (30), attack (15), evaluation (15), mitigation (20), framework (15), and practical usefulness (5). Publication venue was not part of the score. It was used only as a tie-breaker, after score and directness, using the original `Quality_Priority`.

## Screening counts

| Item | Count |
|---|---:|
| Total initial selected records | 606 |
| Titles screened | 606 |
| Title-stage Include | 221 |
| Title-stage Exclude | 193 |
| Title-stage Uncertain | 192 |
| Abstracts screened | 413 |
| Abstract-stage Include | 232 |
| Abstract-stage Exclude | 141 |
| Abstract-stage Uncertain | 4 |
| Missing abstracts (among abstracts screened) | 36 |
| Final selected papers | 100 |
| Reserve eligible papers | 132 |

Record check: 100 final + 132 reserve eligible + 4 uncertain + 36 missing abstracts + 141 abstract exclusions + 193 title exclusions = 606.

Abstract-stage Include is 232. Of those, 146 scored 58 or higher. The final set is the 100 highest of that group. The other 46 papers at or above 58, and the 86 included papers below 58, are in the reserve workbook with status `Reserve_Eligible` (132). The cutoff was not lowered to force a count, and papers above the cutoff were not dropped below 100: more than 100 cleared the bar, so the primary set is the top 100.

The highest score is 83 and the lowest score in the final set is 62. Rank 1 is ACE: A Security Architecture for LLM-Integrated App Systems.

## Research dimension distribution

Primary dimension of the 100 final papers, assigned from the highest component score:

| Primary dimension | Papers |
|---|---:|
| Attack | 32 |
| Evaluation Metrics/Benchmarks | 18 |
| Mitigation | 35 |
| Proposed Framework | 15 |

A paper is filed under `Multi_Dimensional/` when at least two components are strong (attack or evaluation at least 10, mitigation at least 12, or framework at least 10). That is 54 papers. The other 46 stay in the folder of their primary dimension: Attack 20, Evaluation_Benchmarks 10, Mitigation 11, Framework 5.

Counting a paper once for its primary dimension and again for each secondary dimension that scored at least 6 gives: Attack 74, Evaluation 76, Mitigation 68, Framework 83. Those figures overlap on purpose. Mitigation is the largest primary category.

## Publication quality distribution

Original verified categories, unchanged:

| Quality category | Final papers |
|---|---:|
| CORE A / CCF A Conference* | 44 |
| CORE A / CCF B Conference | 4 |
| CORE B / CCF C Conference | 7 |
| CORE C Conference | 2 |
| Other peer-reviewed conferences and workshops | 43 |

Corresponding quality levels: Top 44, Very High 4, Good 7, Moderate 2, Lower 43.

## PDF retrieval

Retrieval was attempted for all 100 final papers. Lookups used OpenAlex open-access locations, arXiv links already stored on the record, and the ACL Anthology PDF that corresponds to a `10.18653/v1` DOI. Unpaywall rejected the request email, so it was not used for the successful downloads. No paywall was bypassed. A file was kept only if it was a PDF, opened, and its extracted text or metadata matched the selected title. Mismatches were not saved.

| Outcome | Count |
|---|---:|
| Total selected papers | 100 |
| Total retrieval attempts | 100 |
| Official proceedings PDFs downloaded | 41 |
| Publisher journal PDFs downloaded | 0 |
| Author manuscripts downloaded | 0 |
| Verified preprints | 27 |
| Paywalled, no open PDF located | 31 |
| Access denied | 1 |
| Not found, other than the paywalled set | 0 |
| Invalid or mismatched files kept | 0 |

Proceedings copies are 35 from the ACL Anthology, 4 from NDSS via the publisher DOI, and 2 from the AAAI proceedings site. The 27 preprints are arXiv files whose titles matched the selected records. They are labeled preprints, not versions of record.

The access-denied paper is `P000751` (SecureGov-Agent). The only open location returned HTTP 403.

Local files were reopened after download. All 68 saved files begin with the PDF header and are larger than 4 KB. Paths are listed in `05_Full_Texts/Final_PDF_Verification.xlsx`.

## Validation

- Every final paper has title decision Include or Uncertain, abstract decision Include, a score, a rationale, and a rank.
- No final paper lacks an abstract.
- Ranks follow score, then directness, then original quality priority, then year.
- Quality category and quality priority were copied from the source workbook.
- Paper IDs in the final sheet are the original IDs, and the 100 DOIs are unique.
- The reserve register contains the other 506 records.
- Every final paper has one retrieval attempt, and every successful download exists at the path in the verification workbook.
