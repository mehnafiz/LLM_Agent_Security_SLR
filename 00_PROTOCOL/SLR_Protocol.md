# SLR protocol

Date of this consolidation: 2026-11-03.

## Sources

- IEEE workbook `LLM_Agent_Security_Literature_Collection.xlsx`, sheet `All_Collected_Papers` (164 rows).
- Google Scholar workbook `Google_Scholar_Best_Related_LLM_Agent_Security.xlsx`, sheet `All_Related` (270 rows).
- Downloaded PDFs in `TOP_RELATED_PAPER/` (copied, not moved).
- Identity-checked PDFs already stored under `LLM_Agent_Security_SLR/full_text/verified/` (read-only).

Original workbooks are not edited. Zotero the application is not written to. `07_ZOTERO/PRE` and `07_ZOTERO/POST` are the bibliographic snapshots prepared for a later import.

## Identification and deduplication

PRE stacks both paper tables (434 rows). POST keeps one row per exact DOI, or per exact normalized title when no DOI is present. When both sources share that key, the IEEE row is the bibliographic master and the Scholar row is recorded on the removal log (15 removals; 419 remaining). Fuzzy near-duplicates are not auto-merged.

## Screening stance

Earlier title, abstract, and full-text labels in the historical project are suggestions. This folder does not re-label them as final human decisions. Final eligibility still requires a publisher version and venue-quality evidence.

## Synthesis

Analysis fields are filled only from text that was extracted from a retrieved PDF. Empty cells stay empty or `Not Reported`. AgentShield-LCE is design text, not an experimental result.
