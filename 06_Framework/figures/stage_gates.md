# Stage gates

A gate is a pass or fail check on the evaluation record. It is not a component on the agent’s request path. It does not add serving latency, and it does not re-check a decision the agent has already made at runtime. Runtime checks are the controls in `Mitigation_Strategy.md`.

A waiver is written into the Stage 10 record. A waiver is not a pass. A waived surface is absent from the metric table.

Figure 4 draws the four decisions and their return paths.

| Gate | After | Evidence required | Pass | Fail |
|---|---|---|---|---|
| G1 | Stage 2 | The catalog covers, or waives in writing, each of: instruction channel, untrusted content, tool description, tool code, memory, and peer agents. A conditional actor that is not in the asset register is waived, not silently dropped | Every surface is covered or waived, and each covered surface has an adversary, a goal, and a precondition | Return to Stage 2. Do not write tests |
| G2 | Stage 5 | Every case has a trace containing tool name, arguments, tool result, committed flag, memory operation, and outbound destination, or a recorded runner failure. Plan text, if stored, is marked as a non-oracle | The trace set matches the manifest. Runner failures are counted apart from scores | Return to Stage 5. A missing tool log is not a score |
| G3 | Stage 6 | Every reported number cites a trace field and a requirement identifier. Task success uses the same pairs as attack success. The carrier is one the system reads. Empty successful-attack sets leave detection coverage and false negatives undefined | All five questions in `Evaluation_Protocol.md` are answered, and item 3 is yes | Return to Stage 4 when the check or the carrier was wrong. Return to Stage 6 when only the arithmetic was wrong |
| G4 | Stage 8 | Every control under test has a class, an observation point, the requirement identifiers it covers, task success on the baseline and protected runs, and the leftover identifiers. The changed-attack manifest has been rerun, or a waiver states why it was not | The before-and-after table contains those fields | Return to Stage 8. A control without a rerun is not finished |

## What a failure does not do

- G1 does not delete a surface to make the catalog look complete. It sends the catalog back.
- G2 does not impute a tool call from the model’s final sentence.
- G3 does not accept a lower attack-success number as a substitute for a missing citation.
- G4 does not treat a fall in attack success as completion when task success is unreported or leftovers are unnamed.
- No gate asks a person to approve the evaluation in order to convert a fail into a pass. Human approval of a tool call is a respond control inside the run, and it is scored like any other control.

## Duplication

G2 checks that the trace exists. G3 checks that the arithmetic uses that trace. They are different tests. G4 checks the control record. It does not rescore the trace. Stage 9 checks restoration. It is not a gate, because an irreversible tool has no pass condition other than an honest residual.

## Figure 4

**Caption.** Figure 4. Stage-gate decisions. Each decision node states the condition. A pass continues downward. A fail returns to the stage that can repair the missing evidence. The left-hand arrow sends the next change of the agent from Stage 10 back to Stage 2. The nodes are evaluation checks, not runtime interlocks.
