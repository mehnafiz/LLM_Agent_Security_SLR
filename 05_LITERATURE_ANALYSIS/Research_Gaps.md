# Research gaps

These gaps are the ones that forced the shape of AgentShield-LCE. They are stated only where the extracted full texts and the source tables already show the split.

1. **Oracle gap.** Attack success is often a model-judged string. The traces needed to show a tool effect, a memory write, or an exfiltration are not part of the score.
2. **Utility gap.** Defenses are compared on attack success without the paired benign task, so a refusal-everything policy looks strong.
3. **Memory gap.** Prompt-injection benches are more common than tests that poison memory, wait, and measure a later session.
4. **Tool-metadata gap.** Tool-description poisoning is measured separately from runtime permission checks, so a passing injection defense can still follow a poisoned manual.
5. **Monitor gap.** Detectors are reported on one attack distribution. Coverage after the attacker changes the distribution is rarely a required table.
6. **Recovery gap.** Papers that detect a bad memory entry rarely re-run the suite after deletion to show the entry is gone and the task still works.
7. **Multi-agent gap.** Agent-to-agent protocols, malfunction amplification, and psychological manipulation do not share a metric with single-agent tool injection, so a lifecycle cannot add them up.
8. **Benchmark-validity gap.** A suite can score the wrapper of an attack template rather than the attack. The protocol therefore refuses a metric that does not point at a trace field.
9. **Venue-evidence gap.** This project cannot yet mark a large eligible set, because publisher version and quartile evidence are missing for most relevant PDFs. That is a gap in the review’s evidence, not a reason to relax the rule.
