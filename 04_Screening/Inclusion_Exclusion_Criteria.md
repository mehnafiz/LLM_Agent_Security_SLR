# Inclusion and exclusion criteria for study selection

**Table 2** (Excel + figure):
- `04_Screening/Inclusion_Exclusion_Criteria.xlsx`
- `04_Screening/Inclusion_Exclusion_Criteria.png`

These criteria decide which records enter the ranked selected set. They follow the same screening practice as `Title_Abstract_Screening_and_PDF_Retrieval_Report.md`.

## Table 2. Inclusion and exclusion criteria for study selection

| Inclusion criteria | Exclusion criteria |
|---|---|
| **IC1.** The study addresses security of LLM-based agents: attacks, adversarial/red-team testing, defenses, evaluation metrics or benchmarks, taxonomies, or security frameworks for agents. | **EC1.** Repository-only or non-peer-reviewed postings with no identified peer-reviewed counterpart, including arXiv, bioRxiv, SSRN, ResearchGate, Zenodo, OSF, or Authorea-only records set aside at quality filtering. |
| **IC2.** The evaluated system is an agentic AI system (tool-using LLM agent, memory-augmented agent, RAG agent, multi-agent system, or MCP/tool-ecosystem agent), not a chat-only LLM. | **EC2.** Vendor blogs, industry white papers, marketing pages, or undocumented reports with no independently verifiable scholarly method. |
| **IC3.** The paper contributes a method or evidence base: an attack, defense, benchmark/dataset, measurement study, taxonomy, tool, architecture, or evaluation protocol—not opinion-only commentary. | **EC3.** Chat-only jailbreaks, prompt injection, or LLM safety work that never involves tools, memory, retrieval, multi-agent messaging, or another agent action surface. |
| **IC4.** The record is a peer-reviewed scholarly publication retained after quality filtering. Accepted sources include: • Primary scholarly databases and indexes used in collection (e.g., Scopus, Web of Science, IEEE Xplore, OpenAlex). • Peer-reviewed digital libraries and proceedings hosts (e.g., ACL Anthology, ACM DL, ScienceDirect, SpringerLink, Wiley). • Ranked or verified peer-reviewed venues after CORE cross-check (e.g., IEEE/ACM conferences, NDSS, IEEE S&P, USENIX Security, ACL, EMNLP, AAAI, NeurIPS, ICML, ICLR, and other CORE-listed or peer-reviewed conference/workshop proceedings). | **EC4.** Non-security agent applications, or papers that use agents only as offensive tools against ordinary software/networks without evaluating the LLM agent’s own security. |
| **IC5.** The study was published in 2024 or later, covering the recent LLM-agent security period. | **EC5.** Traditional network/software penetration testing, classical adversarial ML, or military red teaming with no generative or agentic AI system as the target; studies before 2024; or records with no usable abstract when abstract scoring was required. |

## Venue and archive policy (explicit)

| Rule | Practice in this review |
|---|---|
| Peer-reviewed venues | Included after quality filtering and CORE cross-check (**IC4**). |
| arXiv / bioRxiv / SSRN / ResearchGate / Zenodo / OSF / Authorea | Repository-only records with **no peer-reviewed counterpart** were excluded at quality filtering (**EC1**). |
| Open arXiv PDF for a selected paper | Allowed only as a **title-verified full-text copy** of an already-selected record; labeled preprint, not version of record. |
| Blogs / white papers / marketing | Excluded (**EC2**). |

## Relation to PRISMA counts

| Stage | Link to Table 2 |
|---|---|
| 4,500 → 3,059 | Duplicate removal (not IC/EC). |
| 3,059 → 606 | Quality/venue filter (**IC4**, **EC1**, **EC2**). |
| 606 → 100 | Title/abstract relevance (**IC1–IC3**, **IC5**, **EC3–EC5**). |
| 100 → 71 | Open full-text coding access—not a second relevance filter. |

## Short form

| Code | Criterion |
|---|---|
| IC1 | Topic = LLM-based agent security |
| IC2 | System = agentic (tools / memory / RAG / multi-agent / MCP) |
| IC3 | Contribution = method, benchmark, measurement, taxonomy, tool, or architecture |
| IC4 | Venue = peer-reviewed / quality-filtered scholarly publication |
| IC5 | Year ≥ 2024 |
| EC1 | arXiv/repository-only, no peer-reviewed counterpart |
| EC2 | Blog / white paper / marketing |
| EC3 | Chat-only jailbreak / no agent-action surface |
| EC4 | Non-security agents, or agents only as offensive tools |
| EC5 | Classical non-AI security/AML; pre-2024; missing abstract when required |
