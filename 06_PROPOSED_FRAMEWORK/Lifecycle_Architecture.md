# Lifecycle

Read `Framework_Design.md` first. This file is the operating view: order, fail routes, and what each stage keeps.

```mermaid
flowchart TB
  S1[1 Identify] --> S2[2 Threat model]
  S2 --> G1{G1}
  G1 -->|pass| S3[3 Requirements]
  S3 --> S4[4 Tests]
  S4 --> S5[5 Run]
  S5 --> G2{G2}
  G2 -->|pass| S6[6 Score]
  S6 --> G3{G3}
  G3 -->|pass| S7[7 Detect]
  S7 --> S8[8 Mitigate]
  S8 --> G4{G4}
  G4 -->|pass| S9[9 Recover]
  S9 --> S10[10 Report]
  G1 -->|fail| S2
  G2 -->|fail| S5
  G3 -->|fail| S4
  G4 -->|fail| S8
  S10 -->|next change| S2
```

## Stage sheet

| Stage | Inputs | Work | Outputs | Evidence kept |
|------:|--------|------|---------|---------------|
| 1 Identify | System description | List model, tools, memory, peer agents, and data they can touch. Mark which inputs are untrusted. | Asset register | Register |
| 2 Threat model | Register | For each surface, write adversary, goal, and precondition. | Surface catalog | Catalog |
| 3 Requirements | Catalog | Write "must not" and "must still" in pairs, so a defense cannot win by refusing every task. | Requirement IDs | Requirement list |
| 4 Tests | Requirement IDs | Build a benign case and an attack case with the same user task. Declare the check in advance. | Test manifest | Manifest |
| 5 Run | Manifest | Sandbox tools. Log the plan, tool name, arguments, tool result, memory read/write, and outbound message. | Trace per case | Traces |
| 6 Score | Traces | Count a success only when the pre-declared check fired. Report the benign task beside it. | Metric table | Table plus checklist |
| 7 Detect | Metric table | Mark whether a monitor saw the attack before the effect. | Coverage report | Report |
| 8 Mitigate | Coverage report | Add a control, rerun the same pairs, record what remains. | Before/after table | New traces |
| 9 Recover | Leftover failures | Restore memory and tool side effects. Rerun failures and a sample of earlier passes. | Reassessment | Restore log |
| 10 Report | All of the above | Freeze versions, definitions, and residuals. | Release record | The record |

## Fail routes

| Gate | If it fails |
|------|-------------|
| G1 after Stage 2 | Return to Stage 2. Do not write tests for a surface you have not named. |
| G2 after Stage 5 | Return to Stage 5. A missing tool log is not a score. |
| G3 after Stage 6 | Return to Stage 4 when the check was wrong, or stay in Stage 6 when only the arithmetic was wrong. |
| G4 after Stage 8 | Return to Stage 8. A control without a rerun is not finished. |

Stage 10 always sends the next agent change back to Stage 2. Stages are not skipped to save a number.
