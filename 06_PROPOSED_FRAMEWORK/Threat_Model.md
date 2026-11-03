# Threat model

This is the Stage 2 catalog. Scope: an agent that plans in natural language and then calls tools, writes memory, or messages another agent.

A chatbot jailbreak that never reaches a tool, a memory store, or a second agent is out of scope. An attack on the machine that hosts the model is out of scope unless that machine is part of the system under test.

## Assets

| Asset | What a failure looks like |
|-------|---------------------------|
| User data | A tool or message sends a secret the user did not ask to send |
| Tool effect | The agent calls a tool, or uses arguments, the user did not authorize |
| Memory | A later task follows a poisoned entry, or leaks a stored secret |
| Other agents | A peer message causes a tool call the user did not request |
| User task | The original task fails or is silently replaced |

## Who can attack

- Someone who can place text the agent will read: a web page, an email, a tool description, a retrieved memory entry.
- Someone who publishes a tool whose description or code does not match the user task.
- Another agent in the same system.
- Someone who can poison the traces used to train or fine-tune tool use. Only in scope when that supply chain is part of the system under test.

## Surfaces and the check that would prove an attack

| Surface | Example | The check looks at |
|---------|---------|--------------------|
| Tool result or web page | Indirect prompt injection | The later tool call or message |
| Tool description | A poisoned manual | Which tool was selected |
| Memory | Poisoned or private memory | A later read, write, or leak |
| Peer message | Agent-to-agent manipulation | The receiving agent's tool call |
| Tool code | A backdoored tool | An effect with no matching user request |

## Assumption

The evaluator can sandbox tools and read traces. If tool calls cannot be logged, Gate G2 fails. The run is not reported as an evaluation.
