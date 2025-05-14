# Tools

One crucial aspect of AI Agents is their ability to take actions. 
> As we saw, this happens through the use of `Tools`.

By giving your `Agent` the right `Tools` — and clearly describing how those `Tools` work — you can dramatically increase what your AI can do. 

## What are AI `Tools`?

A `Tool` is a `function` given to the LLM. This `function` should fulfill a clear objective.

If your agent needs up-to-date data you must provide it through some tool. 
> Because their internal knowledge only includes events prior to their training

### A Tool should contain:

* A textual description of what the function does (what we want the LLM to know about the tool.).
* A Callable (something to perform an action).
* Arguments with typings.
* (Optional) Outputs with typings.

An Agent that handles the entire execution process in the background. Understand the context, plan and excute the action (tool), appends a new message (returned by the tool), and LLM processes this additional context to produce a natural-sounding response.

## MCP (Model Context Protocol)

MCP is an `open protocol` that standardizes how applications **provide tools to LLMs**. 

MCP provides:

* A growing list of pre-built integrations that your LLM can directly plug into
* The flexibility to switch between LLM providers and vendors
* Best practices for securing your data within your infrastructure

> This means that any framework implementing MCP can leverage tools defined within the protocol, eliminating the need to reimplement the same tool interface for each framework.

## Summary


To summarize, we learned:

* **What Tools Are:** Functions that give LLMs extra capabilities, such as performing calculations or accessing external data.

* **How to Define a Tool:** By providing a clear textual description, inputs, outputs, and a callable function.

* **Why Tools Are Essential**: They enable Agents to overcome the limitations of static model training, handle real-time tasks, and perform specialized actions.

> Tools play a crucial role in enhancing the capabilities of AI agents.

## Quiz

Q1: Which of the following best describes an AI tool?
> An executable process or external API that allows agents to perform specific tasks and interact with external environments

Q2: How do AI agents use tools as a form of “acting” in an environment?
> By asking the LLM to generate tool invocation code when appropriate and running tools on behalf of the model

Q3: What is a Large Language Model (LLM)?
> A deep learning model trained on large amounts of text to understand and generate human-like language

Q4: Which of the following best describes the role of special tokens in LLMs?
> They serve specific functions like marking the end of a sequence (EOS) or separating different message roles in chat models

Q5: How do AI chat models process user messages internally?
> They convert user messages into a formatted prompt by concatenating system, user, and assistant messages