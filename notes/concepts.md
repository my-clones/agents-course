# Concepts

## Agent

Agent is: an **AI model capable of reasoning, planning, and interacting with its environment.**

User request: → REASON → PLAN → ACT (Agentt's List of known tools)

More formal way.

"An Agent is a system that leverages an **AI model** to **interact** with its **environment** in order to **achieve a user-defined objective**. 
It combines:
1. reasoning, 
2. planning, and 
3. the execution of actions (often via external tools) to fulfill tasks."

---

Agent process:

```mermaid
flowchart LR
    A[User Request]:::noteStyle
    B[Reason]
    C[Plan]
    D[Act]

    A--> B --> C --> D

    classDef noteStyle fill:#fff5c2,stroke:#333,stroke-dasharray: 5 5;
```



```mermaid
flowchart TB
    %% Define Styles
    classDef highlighted_A fill:#5fffd7,stroke:#808080,stroke-width:1px;
    classDef highlighted_B fill:#5fffff,stroke:#808080,stroke-width:1px;

    A[AI Model]:::highlighted_A
    B[List of tools]:::highlighted_B

    A
    B
```

---

LLM - Takes Text as an input and outputs Text as well.

```mermaid
flowchart LR
    %% Define Styles
    classDef class_A fill:#dadada,stroke:#626262,stroke-width:1px,text:bold;
    classDef class_B fill:#5fffd7,stroke:#808080,stroke-width:1px;
    classDef noteStyle fill:#fff5c2,stroke:#333,stroke-dasharray: 5 5;

    A[text]:::class_A
    B[LLP]
    C[text]:::class_A
    
    A --> B --> C
```

---


🔶 BRAIN → **AI model (LLM/BLM)**: 
decision process: which Actions to take based on the situation (reasoning & planning)

🔶 BODY  → **Capabilities and Tools**
Scope of **possible actions** depends on what the agent has been equipped with

> Note that Actions are not the same as Tools. 
> An Action, for instance, can involve the use of multiple Tools to complete.

An Agent is a system that uses an AI Model (typically an LLM) as its core reasoning engine, to:

* Understand natural language: Interpret and respond to human instructions in a meaningful way.
+ Reason and plan: Analyze information, make decisions, and devise strategies to solve problems.
* Interact with its environment: Gather information, take actions, and observe the results of those actions.

---

Quiz

Q1: Which of the following best describes an AI Agent?
> An AI model that can reason, plan, and use tools to interact with its environment to achieve a specific goal.

Q2: What is the Role of Planning in an Agent?
> To decide on the sequence of actions and select appropriate tools needed to fulfill the user’s request.

Q3: How Do Tools Enhance an Agent’s Capabilities?
> Tools provide the Agent with the ability to execute actions a text-generation model cannot perform natively, such as making coffee or generating images.

Q4: How Do Actions Differ from Tools?
> Actions are the steps the Agent takes, while Tools are external resources the Agent can use to perform those actions.

Q5: What Role Do Large Language Models (LLMs) Play in Agents?
> LLMs serve as the reasoning 'brain' of the Agent, processing text inputs to understand instructions and plan actions.

Q6: Which of the Following Best Demonstrates an AI Agent?
> A virtual assistant like Siri or Alexa that can understand spoken commands, reason through them, and perform tasks like setting reminders or sending messages.

