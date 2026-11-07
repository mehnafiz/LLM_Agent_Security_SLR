# Mitigation

A control counts only when it has a class, an observation point, a mechanism, a protected property, a rerun on the same pairs, and a leftover list. Publishing a detector without a prevent, respond, or recover action is a detect result. It is not a claim that the effect was stopped.

The mechanisms below are design controls. Several of them host techniques already reported in the retrieved PDFs. Hosting a technique does not transfer that paper’s measurements to this lifecycle, and it does not make the technique a contribution of AgentShield-LCE.

## Classes

| Class | When it acts | Fair claim | Rerun required |
|---|---|---|---|
| Prevent | Before the effect commits | The forbidden effect did not occur | The full paired suite |
| Detect | During the run, at a named boundary | The case was flagged, and whether the flag preceded the commit | Successful attacks and the benign cases, using the same detector |
| Respond | After a flag | The effect was blocked, or a person approved that call | The same cases, plus the change in task success |
| Recover | After the effect or a suspected poison | State matches the clean baseline, or the irreversible difference is listed | Failed identifiers and a sample of earlier passes |

Prevent stops the effect. Detect notices it. Respond acts on a notice. Recover cleans state. A confirmation prompt is a respond control. It does not replace an allow-list, because an unattended agent cannot wait on a person.

## Control catalog

Figure 5 is this catalog drawn as a matrix. The limitation column is part of the control, not an afterword.

| ID | Threat | Point | Class | Mechanism | Property | Limitation |
|---|---|---|---|---|---|---|
| C1 | Indirect prompt injection from untrusted content | Tool execution, before the result is treated as an instruction | Prevent | Keep the tool result, page, email, or retrieved passage in a data channel. Do not concatenate it into the instruction channel. A filter that deletes instruction-shaped spans from that data is one implementation, not a required component | Integrity of the user task | An adaptive injection can avoid the filter pattern. Benign instructions that the task needed from the data can be removed. Either failure stays in the leftover list |
| C2 | Unauthorized tool use, including instruction-channel abuse and exfiltration | Tool execution, before commit | Prevent | Allow only tool names declared for that requirement. Constrain arguments and outbound destinations to predicates declared in Stage 4 | Authorization and confidentiality | A wide predicate accepts an attacker-chosen argument that still matches. The predicate is then wrong, and G3 returns the case to Stage 4 |
| C3 | Tool-description poisoning | Configuration and tool selection | Prevent | Call a tool only when its description hash matches the pin in the register | Integrity of tool selection | A pin does not make a malicious tool benign. It freezes the manual the evaluator chose to trust |
| C4 | Tool-code backdoor or an effect the description does not show | Tool execution | Prevent | Call the implementation only when its hash and permission match the pin. Deny the call if tool code is in scope and unpinned | Authorization and integrity | Out of scope when Stage 1 waives tool code. A matching hash can still be a tool the user should not have trusted |
| C5 | Indirect injection that changes the plan after untrusted data, and hidden intermediate actions | Planning, compared with the later call | Detect | If a plan was emitted before the untrusted read, flag a later tool call that the plan did not contain | Integrity | A plan written after the poison can be consistent with the attacker’s goal and will not be flagged. This control does not prevent the call |
| C6 | Any committed effect that should have been stopped | Tool execution, at commit | Detect and respond | Flag the call at the commit boundary. Respond by not committing, or by asking for approval of that call | Authorization | A fixed flag misses attacks outside the patterns it encodes. G4 therefore requires a changed-attack rerun or a waiver. Approval of every call is not an allow-list |
| C7 | Memory poisoning | Memory write and later read | Prevent and detect | Accept a write only from carriers the write policy names. On read, check the stored provenance label and quarantine a label that does not match | Integrity of memory | Provenance shows origin. It does not show that the text is harmless. Semantic harm still needs the attack check |
| C8 | Memory disclosure | Memory read followed by an outbound call | Prevent | The destination constraint of C2 applies to data read from memory | Confidentiality | A permitted tool can still leak data if the destination predicate is broader than the task |
| C9 | Peer-caused tool use | Peer exchange | Prevent, detect, and respond | A peer message may name only tools in the peer allow-list. A message that would cause any other tool is flagged and dropped | Authorization | This does not verify an agent-to-agent protocol implementation. The score is not added to single-agent attack success |
| C10 | Poisoned memory or a reversible tool effect | After commit | Recover | Quarantine or delete the entry, roll back a reversible tool effect, restore the clean baseline, and rerun the failed identifiers plus a sample of earlier passes | Integrity, after the fact | Irreversible effects remain residuals. A restore that is not rerun is not recovery |

C1 is the class of instruction and data separation. Published filters are examples of an implementation. C5 is the class of plan-to-call consistency. C3 and C4 are pins, not a general supply-chain audit. C6 is the class of commit-time monitoring. None of these identifiers denotes a new algorithm.

## Properties

The property names are used only as follows.

- **Confidentiality.** User data or memory content is not sent to a destination outside the predicate for that requirement.
- **Integrity.** The tool effect and the memory state match the user task and the pinned tool.
- **Authorization.** The tool name, arguments, and any peer-caused call stay inside the allow-list for that requirement.
- **Availability.** The benign check still holds. This is the user task, not server uptime.

## Changed attacks

Stage 8 is not finished when attack success falls on the original manifest. The record lists:

- requirement identifiers that still fail;
- task success on the baseline run and on the protected run;
- which of the four classes was not implemented;
- either coverage and false positives on a second attack manifest declared before the rerun, or a waiver that states why the original distribution is the only one in scope.

The second manifest exists because disclosed defenses and fixed monitors have failed when the attack pattern changed. Those are findings of the papers that ran the tests. This lifecycle requires the rerun or the waiver. It does not claim that the rerun restores coverage.

## What is not in this file

This file does not rank published defenses. It does not assign a residual-risk score. Per-paper notes stay in `05_LITERATURE_ANALYSIS/Paper_Analysis_Matrix.xlsx`, and only in cells taken from text that was read.

## Figure 5

**Caption.** Figure 5. Mapping from attack category to control. Each row names the observation point, the class, the mechanism, the property, and the limitation that remains. The matrix matches the catalog in this file. It does not show measured reductions.
