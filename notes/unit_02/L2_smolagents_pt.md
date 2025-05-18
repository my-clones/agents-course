
# smolagents

É um framerwork para desenvolvimento de agentes inteligentes.

smolagents oferece:

* **Simplicidade**: abstração de detalhes sobre desenvolvimento de agentes inteligentes.
* **Integração com o HF Hub**: permite compartilhar ou usar ferramentas e agentes do HF Hub.
* **Agnóstico ao modelo**: suporta qualquer modelo.
* **Agnóstico à modalidade**: suportta texto, imagens e audio.
* **Independente de ferramenta**: pode usar ferramentas de MCP, LangChain etc.

> Em smolagents, as ferramentas são definidas usando o decorador `@tool`, que envolve uma `função` Python ou a `classe Tool`.
---

Recursos:

* [smolagents Documentation](https://huggingface.co/docs/smolagents/index) - Official docs for the smolagents library
* [smolagents blog](https://huggingface.co/blog/smolagents) - Blog about smolagents
* [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - Research paper on agent architectures
* [Agent Guidelines](https://huggingface.co/docs/smolagents/tutorials/building_good_agents) - Best practices for building reliable agents
* [LangGraph Agents](https://langchain-ai.github.io/langgraph/) - Additional examples of agent implementations
* [Course on LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) - Full course on LangGraph from LangChain
* [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling?api-mode=responses) - Understanding function calling in LLMs
* [RAG Best Practices](https://www.pinecone.io/learn/retrieval-augmented-generation/) - Guide to implementing effective RAG
* [Code Agents](https://huggingface.co/docs/smolagents/en/conceptual_guides/intro_agents#code-agents): why code agents are effective
* [Paper](https://huggingface.co/papers/2402.01030):  Executable Code Actions Elicit Better LLM Agents
* [Secure code execution](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution): how to secure code execution
* [opentelemetry](https://opentelemetry.io/training/): Open Telemetry course


---

## smolagents tipos de agentes

**1️⃣ CodeAgents**

> **`CodeAgents`** são o principal tipo de agente em smolagents. 

Em vez de gerar *`JSON`* ou *`text`*, esses agentes **produzem código `Python`** para executar ações. 

> o smolagents se concentra em chamadas de ferramentas no código, simplificando o processo de execução, podendo chamara execução do código diretamente.


**3️⃣ ToolCallingAgents**

`ToolCallingAgents` são o segundo tipo de agente suportado por smolagents. 

(Ao contrário dos CodeAgents, que geram código Python)

Esses agentes dependem de `JSON/blobs` de texto que o sistema deve analisar e interpretar para executar ações.

**4️⃣ *Tools* (Ferramentas)**

Ferramentas são `funções` que um `LLM` pode usar em um `agentic system` e atuam como blocos de construção essenciais para o comportamento do agente. 

> classe **`Tool`** ou o decorador **`@tool`**. 

Ver como: 
* funcionam a `default toolbox`, 
* **compartilhar** `ferramentas` com a comunidade, e 
* **carregar** `ferramentas` contribuídas pela comunidade para uso em seus agentes.

**5️⃣ RetrievalAgents**

> ***Agentes de recuperação*** permitem que modelos **acessem bases de conhecimento** 

* ajudam a **buscar**, **analisar** e **recuperar** **informações** de várias fontes
  * mantendo o **contexto da conversa** com o uso de um **`memory sustem`**.
* utilizam `VectorDBs` / fluxos de `RAG` ara uma recuperação eficiente de informações.  
* implementam **técnicas avançadas de *Information Retrieval*** para aumentar a robustez do sistema, incluindo políticas de **fallback** que garantem continuidade mesmo em cenários de falha parcial ou ausência de resultados relevantes.


**6️⃣ Multi-Agent Systems**

> Orquestrar múltiplos agentes de forma eficaz é crucial para a construção de sistemas multiagentes mais poderosos. 

Combinar agentes com diferentes capacidades — como um agente de busca na web com um agente de execução de código — você pode criar soluções mais sofisticadas. 

**7️⃣ Vision and Browser agents**

Os agentes de visão ampliam as capacidades tradicionais dos agentes, incorporando Modelos de Visão e Linguagem (VLMs), permitindo que processem e interpretem informações visuais.

Funcionalidades avançadas como: 
* raciocínio baseado em imagens, análise visual de dados e interações multimodais. 
* um agente de navegador que pode navegar na web e extrair informações dela.

## Devo usar `smolagents` quando:

* precisar de uma solução leve e minimalista.
* precisar fazer um prtótipo, sem configurações complexas.

## Multistep agents

Cada MultiStepAgent executa:
- Un pensamento
- Una chamada e execução de ferramenta



## Integração de Modelos em smolagents

O smolagents suporta integração LLM flexível, permitindo que você use qualquer modelo invocável que atenda a determinados critérios. O framework fornece várias classes predefinidas para simplificar as conexões de modelos:

* **TransformersModel**: Implementa um pipeline local de transformadores para integração perfeita.
* **InferenceClientModel**: Suporta chamadas de inferência sem servidor por meio da infraestrutura da Hugging Face ou por meio de um número crescente de provedores de inferência de terceiros.
* **LiteLLMModel**: Utiliza o LiteLLM para interações leves com modelos.
* **OpenAIServerModel**: Conecta-se a qualquer serviço que ofereça uma interface de API OpenAI.
* **AzureOpenAIServerModel**: Suporta integração com qualquer implantação do Azure OpenAI.

> Essa flexibilidade garante que os desenvolvedores possam escolher o modelo e o serviço mais adequados para seus casos de uso específicos e permite fácil experimentação.
