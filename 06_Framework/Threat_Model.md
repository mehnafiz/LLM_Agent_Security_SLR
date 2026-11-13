# Threat model

This is the Stage 2 catalog. Scope is the agent path in `Lifecycle_Architecture.md`: an agent that plans in natural language and then calls tools, writes memory, or messages another agent.

A chatbot jailbreak that never reaches a tool, a memory store, or a second agent is out of scope. An attack on the host machine is out of scope unless that machine is part of the system under test. Figure 3 is this catalog. Figure 2 draws the path the catalog refers to. Neither figure adds an actor that the table omits.

## Assets

| Asset | Failure that counts |
|---|---|
| User data | A tool call or message sends a secret the declared task did not allow to be sent |
| Tool effect | The agent calls a tool, or passes arguments, that the task did not authorize |
| Memory | A later task follows a poisoned entry, or a stored secret is read into an unauthorized send |
| Peer agents | A peer message causes a tool call the user did not request |
| User task | The benign check fails, or the task is replaced by the attacker’s task |

Availability in this catalog means the user task. It does not mean uptime of the model server.

## Actors

Each actor has only the capability stated. A stronger actor is a different row, not an implication.

| Actor | Capability | Not capable of | When included |
|---|---|---|---|
| Content injector | Place text the agent will read: a page, an email, a retrieved passage, or a tool result | Call tools directly; change weights | Always, if any untrusted carrier exists |
| Instruction adversary | Supply the instruction channel | Reach a tool except through the agent | When the check is a tool, memory, or peer effect. Chat-only jailbreak is excluded |
| Tool publisher | Publish a description, an implementation, or both, that the registry may load | Impersonate the user | When the agent installs or selects third-party tools |
| Peer agent | Send a message the receiving agent treats as input | Bypass the receiver’s tool boundary except by that message | When a peer is in the register. Otherwise waived |
| Model or trace supplier | Poison weights or tool-use traces before deployment | Act at runtime without a trigger in an in-scope carrier | Only if that supply chain is in the register |
| Internal evolution | Write memory, tool entries, or workflow that a later session will trust | An external party is not required | Only if the system updates itself between tasks. Otherwise waived |

The content injector, the tool publisher, and the peer agent are established by the retrieved corpus: indirect injection through external content, tool-description poisoning distinct from tool code, and agent-to-agent protocol attacks. The instruction adversary is a design inclusion and has weaker support in the candidate set. The model supplier and internal evolution are conditional. Candidate papers on backdoors and on self-evolving agents motivate the conditions. They do not put those actors into every evaluation.

## Trust boundaries

| Boundary | Rule |
|---|---|
| TB1 Instruction / data | Instruction and untrusted data are separate channels. A direct instruction remains subject to the task allow-list |
| TB2 Planner / tool | Description, implementation, and permission are separate. Registry membership is not authorization |
| TB3 Agent / memory | Stored text is data until a write policy promotes it |
| TB4 Agent / peer | A peer message cannot authorize a tool the user did not grant |
| TB5 Evaluator / model | The oracle is the trace. The model’s own claim of refusal or compliance is not evidence |

## Surfaces and checks

The check is the predicate Stage 4 must declare. The example is an illustration, not a test payload.

| Surface | Carrier | Established scenario | Check looks at |
|---|---|---|---|
| Untrusted content | Tool result, page, email, retrieved passage | Indirect prompt injection that replaces the task or induces a later call | The later tool call, arguments, or outbound destination |
| Tool description | Manual or schema text | Description poisoning that changes which tool is selected | The selected tool name |
| Tool code | Implementation behind a pinned or unpinned name | An effect with no matching user request | The effect, not the description |
| Memory | Entry written earlier | Poisoned entry followed on a later read; secret disclosed from memory | The later read, write, or outbound send |
| Peer message | Agent-to-agent payload | The receiver calls a tool the user did not request | The receiver’s tool call |
| Instruction channel | User instruction | Unauthorized tool effect requested directly | The tool call. No check is defined for a jailbreak that stops at text |

Privilege separation is not a surface of its own. If the register lists more than one permission level, an attack that uses a higher level than the task allows is an unauthorized tool effect on the tool-code or tool-execution check. If the register has one level, privilege separation is waived at G1.

## Objectives

The attacker objectives this catalog can score are task replacement, unauthorized tool execution, exfiltration of user or memory data, persistence through memory, a peer-caused action, and denial of the user task. An objective that cannot be written as one of the checks above is out of scope for the metric table. It may still be named in the catalog as not scored.

A multi-agent observation that is not a tool-trace predicate is not scored. Forcing it into attack success would add unlike measurements.

## Assumptions

- The evaluator can sandbox tools and can read the trace fields listed in `Lifecycle_Architecture.md`. If those fields cannot be logged, Gate G2 fails. The run is not reported as an evaluation.
- The benign task and the attack task share the user goal. Otherwise utility under attack is undefined.
- A tool that cannot be rolled back can still be tested. Recovery then records an irreversible residual instead of a clean baseline.
- The attacker does not control the instrumentation. An attacker who can forge traces is outside TB5 and outside this model.

## Scope of attack classes

A class is in scope only when its success can be written as a check in the table above. Partial means the trace can show the effect and cannot show the cause. Outside means this lifecycle does not score it. None of these rows is a detection claim.

| Attack class | Placement | Why |
|---|---|---|
| Indirect prompt injection through a carrier the agent reads | In scope | The later tool, memory, or send is the check |
| Direct instruction that requests an unauthorized tool, memory, or peer effect | In scope | The same tool check. The instruction is the carrier |
| Tool misuse, unauthorized execution, and argument or destination abuse | In scope | C2 and the tool-execution check |
| Tool-description poisoning and tool-code effects | In scope when the register includes that surface | Separate checks. A waived surface is not scored |
| Memory poisoning and memory disclosure | In scope when memory is in the register | Write, later read, or outbound send |
| Planning that changes a later call | Partially observable | The call is observable. The plan text is not an oracle |
| Peer-caused tool execution | In scope when a peer is in the register | Scored separately from single-agent results |
| Excessive agency and privilege above the task’s level | In scope only as an unauthorized tool effect | Waived when the register has one permission level |
| Data exfiltration | In scope when the destination is in the trace | The check is the destination, not a guessed intent |
| Chat-only jailbreak | Outside | No tool, memory, or peer effect to score |
| Unobservable change to internal reasoning | Outside | No trace field records hidden state |
| Host, hypervisor, and network compromise | Outside, unless that host is the system under test | Not a listed carrier |
| Multi-agent messages the instrumentation cannot read | Outside | G2 fails if the receiver’s tool call is not logged |
| Training-time or weight backdoors | Conditional | Scored only when that supply chain is in the register |

## Out of scope

- Chat-only jailbreaks.
- Host, hypervisor, and network attacks that do not appear as a listed carrier.
- Training-time poisoning when the training pipeline is not in the register.
- Self-evolution when the agent does not write a later session’s memory, tools, or workflow.
- Attacks invented to fill an unused category. Supply-chain and peer rows are omitted by waiver when the system does not have them, rather than simulated by a prompt pasted into the system message.

## Figure 3

**Caption.** Figure 3. Actors, assets, trust boundaries, and attack surfaces. The user instruction enters the agent. The agent is centered, with a separate link to tools and dashed links to memory and to a peer. Those links are not a path from tools through memory to the peer. Memory and peer appear only when Stage 1 registers them. Conditional actors stay dashed. TB1 is the sentence in the table above. TB5 is the boundary between the evaluator and the model. It is not a network edge. The drawing labels the implementation surface “Tool implementation.” A waiver of tool code is a scope note under the assets, not an attack surface. Gates are not on this figure. An attempt is not the same mark as an observable effect.
