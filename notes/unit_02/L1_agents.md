# Frameworks de Agentes (Agentic Frameworks)

Alguns exemplos de frameworks: `smolagents`, `LlamaIndex` e `LangGraph`.

---

Quando usar um **Agentic Framework**?

Um *agentic framework* oferece flexibilidade para resolver tarefas com **`LLMs`**, mas não é sempre necessário. Em muitos casos, fluxos predefinidos ou fluxos simples de prompts já atendem bem, proporcionando mais controle e menos abstrações.

Porém, quando o fluxo envolve funções dinâmicas ou múltiplos agentes, as abstrações do framework passam a ser úteis e justificadas.

---

**Recursos** fornecidos por um **agentic frameworks**:

`LLM engine` `Tools` `Parser` `System prompt` `Memory` `Error logging`

* Um **LLM engine** que alimenta o sistema.
* Uma **lista de ferramentas** que o agente pode acessar.
* Um ***parser* (analisador sintático)** para extrair chamadas de ferramentas da saída do LLM.
* Um **system prompt** sincronizado com o analisador.
* Um sistema de **memória**.
* **Error logging** para controlar eventuais falhas e erros de LLM. 

---

**Agentic Frameworks**

* **smolagents**: Agents framework developed by Hugging Face.	
* **LlamaIndex**: End-to-end tooling to ship a context-augmented AI agent to production
* **LangGraph**: Agents allowing stateful orchestration of agents

