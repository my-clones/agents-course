# Agentes `agents`
***`Thought`-`Action`-`Observation`.***

Um agente é um sistema que pode 'pensar', planificar e interagir com seu ambiente. Em outras palavras, um agente é definido por ciclos  **`Pensar`-`Agir`-`Observar`** 


* **Pensamento**: A parte `LLM` do `agente` **decide** qual deve ser o **próximo passo**.
* **Ação**: O `agente` realiza uma **ação**, chamando as ferramentas com os argumentos associados.
* **Observação**: O `LLM` **reflete** sobre a resposta da ferramenta.

Os três componentes trabalham juntos em um **loop contínuo** até que o **objetivo do agente seja alcançado** ou um "erro" seja detectado (ex: falha na comunicação).


> 👉 Geralmente, as **regras e diretrizes** são incorporadas diretamente no **prompt do sistema** (`system: ""`), garantindo que cada ciclo obedeça a uma lógica definida.


No **prompt do sistema** (`system: ""`), podemos definir:

* O comportamento do `Agente`.
* As `Ferramentas` às quais nosso Agente tem acesso, conforme descrito na seção anterior.
* O `Ciclo Pensamento-Ação-Observação`, que incorporamos às instruções do LLM.

```python
SYSTEM_PROMPT = """Answer the following questions as best you can. 
You have access to the following tools:

get_weather: Get the current weather in a given location

The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are:
get_weather: Get the current weather in a given location, args: {{"location": {{"type": "string"}}}}
example use :

'''
{{
  "action": "get_weather",
  "action_input": {"location": "New York"}
}}

ALWAYS use the following format:

QUESTION: the input question you must answer
THOUGHT: you should always think about one action to take. Only one action at a time in this format:
Action:
'''

$JSON_BLOB

OBSERVATION: the result of the action. This Observation is unique, complete, and the source of truth.
... (this Thought/Action/Observation can repeat N times, you should take several steps when needed. The $JSON_BLOB must be formatted as markdown and only use a SINGLE action at a time.)

You must always end your output with the following format:

THOUGHT: I now know the final answer

FINAL ANSWER: the final answer to the original input question

Now begin! Reminder to ALWAYS use the exact characters `FINAL ANSWERr:` when you provide a definitive answer. 
"""
```

### Example:

Let’s take a small example to understand the process before going deeper into each step of the process:


***REVIEW THE MERMAID FLOW - PROCESS***

```mermaid
```


**Integração de Ferramentas**
A capacidade de chamar uma ferramenta (como uma API de previsão do tempo) permite que o `agente` Alfred vá além do conhecimento e recupere **dados em tempo real**, um aspecto essencial de muitos Agentes de IA.


**Adaptação Dinâmica**
Cada ciclo permite que o `agente` incorpore novas informações (`observações`) ao seu raciocínio (`pensamento`), garantindo que a resposta final seja bem informada e precisa.

> Este exemplo demonstra o conceito central por trás do ciclo ReAct: 
> A*interação entre `Pensamento`, `Ação` e `Observação` **capacita os agentes de IA** a resolver tarefas complexas iterativamente.

## ReAct

A abordagem **`ReAct`**, uma técnica de prompting que incentiva o modelo a pensar "passo a passo" antes de **`agir`** e antes de permitir que o **`LLM`** decodifique os próximos tokens para resposta final.

Quando um `LLM` é guiado a pensar "passo a passo", envorajando um processo de decodificação em direção aos próximos tokens que geram um plano, em vez de uma solução final, já que o `LLM` é incentivado a decompor o problema em subtarefas antes.

> **🔄 Ciclo ReAct**
> A intereção entre **`Thought`**, **`Action`**, and **`Observation`** capacita os agentes de IA a resolver tarefas complexas de forma iterativa

```mermaid
flowchart LR
    A[User]:::noteStyle
    B[Thought]
    C[Action]
    D[Observation]
    E[User]:::noteStyle

    A--> B --> C --> D --> E
    D --> B

    classDef noteStyle fill:#fff5c2,stroke:#333,stroke-dasharray: 5 5;
```

🔶 Temos visto **recentemente um grande interesse por <u>estratégias de raciocínio</u>**. É isso que está por trás de modelos como o `Deepseek R1` ou o `o1` da OpenAI, que foram **fine-tuned** (aprimorados) para **"pensar antes de responder"**.

Esses modelos foram treinados para sempre incluir **`seções de pensamento`** específicas, entre os tokens especiais **`<think>`** ... **`</think>`**. 

Esta **não é apenas uma técnica de prompt como o ReAct**, **mas um método de treinamento em que o modelo aprende a gerar essas seções** após analisar milhares de exemplos que mostram o que esperamos que ele faça.


### Pensamento (`Thought`)

> 🧠 **Raciocínio Interno do Agente**

Os pensamentos representam o raciocínio interno e os processos de planejamento do agente para resolver a tarefa. 

O **`agente`** utiliza a capacidade do **`LLM`** de analisar informações dispníveus e criar estratégias para atingir seus objetivos. Pense nisso como o diálogo interno do agente, onde ele considera a tarefa em questão e elabora estratégias para sua abordagem. Por meio desse processo, o **`agente`** pode **decompor problemas complexos em etapas menores e mais gerenciáveis**, refletir sobre experiências passadas e ajustar continuamente seus planos com base em novas informações.

**Tipos de Pensamento (exemplos):**

| Tipo | Descrição |
| --- | --- |
| **Planejamento** | “Preciso dividir esta tarefa em três etapas: 1. coletar dados, 2. analisar tendências, 3. gerar relatório” |
| **Análise**  | “Com base na mensagem de erro, o problema parece estar nos parâmetros de conexão com o banco de dados” |
| **Tomada de Decisão** | “Dadas as restrições orçamentárias do usuário, devo recomendar a opção intermediária” |
| **Resolução de Problemas** | “Para otimizar este código, devo primeiro criá-lo para identificar gargalos” |
| **Integração de Memória** | “O usuário mencionou sua preferência por Python anteriormente, então fornecerei exemplos em Python” |
| **Autorreflexão** | “Minha última abordagem não funcionou bem, devo tentar uma estratégia diferente” |
| **Definição de Metas** |“Para concluir esta tarefa, preciso primeiro estabelecer os critérios de aceitação” |
| **Priorização** | “A vulnerabilidade de segurança deve ser corrigida antes da adição de novos recursos” |

### Ação (`Action`)

> ▶️  **Como o agente interaja com seu ambiente**

As ações representam as decisões e acoes do agente para atingir seus objetivos.

### Observação (`Observation`)

> 🧐 ** como um Agente percebe os resultados de suas ações**

As observações representam os resultados das ações e os dados coletados ao longo do processo.


