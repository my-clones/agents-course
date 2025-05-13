# Tools

One crucial aspect of AI Agents is their ability to take actions. 
> As we saw, this happens through the use of `Tools`.

By giving your `Agent` the right `Tools` — and clearly describing how those `Tools` work — you can dramatically increase what your AI can do. 

**What are AI `Tools`?**

A `Tool` is a `function` given to the LLM. This `function` should fulfill a clear objective.

If your agent needs up-to-date data you must provide it through some tool. 
> Because their internal knowledge only includes events prior to their training

**A Tool should contain**:

* A textual description of what the function does (what we want the LLM to know about the tool.).
* A Callable (something to perform an action).
* Arguments with typings.
* (Optional) Outputs with typings.

An Agent that handles the entire execution process in the background. Understand the context, plan and excute the action (tool), appends a new message (returned by the tool), and LLM processes this additional context to produce a natural-sounding response.
