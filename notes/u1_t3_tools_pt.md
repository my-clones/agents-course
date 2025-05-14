# Ferramentas (<i>Tools</i>)

> ✳️ Um aspecto crucial dos Agentes de IA é sua capacidade de realizar ações. 

Ao fornecer ao seu `Agente` as `Ferramentas` certas — e descrever claramente como elas funcionam — você pode **aumentar** drasticamente o **alcance** do `agente`.

**O que são Ferramentas de IA?**
> Uma Ferramenta é uma função atribuída ao LLM. 
> Uma boa ferramenta deve complementar o poder de um LLM.

---
### ⚠️ Importante

Os LLMs preveem a conclusão de um prompt com base em seus dados de treinamento, o que significa que seu conhecimento interno inclui apenas eventos anteriores ao treinamento e não inclui os dados específicos do seu contexto de negócio. 

Se o seu agente precisar de **dados atualizados ou do seu contexto de negócio**, você d**everá fornecê-los**, por meio de RAG ou por meio de alguma ferramenta.

---

### Uma Ferramenta deve conter:

* Uma descrição textual do que a função faz.
* Um *`Callable`*, algo que possa executar uma ação.
* Argumentos com tipagens.
* *(Opcional)* Tipagens das saidas/respostas.

---

### Como funcionas as Ferramentas

Quando falamos em fornecer `ferramentas` a um `agente`, queremos dizer:
* **informar** o 🧠 `LLM` **sobre a existência** dessas `ferramentas` e 
* **instruir** como a **gerar invocações** quando necessário.
  > LLMs só podem receber entradas de texto e gerar saídas de texto.

* o `User` **envia uma mensagem** para o `LLM`
* o `LLM` **gera uma resposta**
* o `Agente` **lê essa resposta**, 
* o `Agente` **identifica** que uma **chamada de ferramenta é necessária**, 
* o `Agente` **executa a ferramenta** em nome do `LLM`
* o `Agente` **pega os dados** retornados pela ferramenta.
* o `Agente` as **anexa esses uma nova mensagem** antes de passar a conversa atualizada para o `LLM` novamente. 
* o `LLM`  **processa esse contexto adicional** e **gera uma resposta** para o usuário. 

> As etapas de chamada da ferramenta normalmente não são mostradas ao usuário.
> Da perspectiva do usuário, parece que o LLM interagiu diretamente com a ferramenta, mas, na realidade, foi o Agente que cuidou de todo o processo de execução em segundo plano.

**Como fornecemos ferramentas para um LLM?**

Basicamente usamos o **prompt do sistema** (`sysmtem:`) para fornecer descrições textuais das ferramentas disponíveis para o `LLM`.

---

## MCP (Model Context Protocol)

O MCP é um **protocolo aberto** que **padroniza** como os **aplicativos fornecem ferramentas para LLMs**.

O MCP oferece:

* Uma lista crescente de **integrações** pré-criadas às quais seu `LLM` pode se conectar diretamente
* A **flexibilidade** para alternar entre provedores e fornecedores de `LLM`
* Melhores práticas para **proteger seus dados** em sua infraestrutura

Isso significa que qualquer estrutura que implemente o `MCP` pode **aproveitar** as ferramentas definidas no protocolo, **eliminando a necessidade de reimplementar a mesma interface de ferramentas para cada estrutura**.

## Resumo

Para resumir, aprendemos:

* **O que são ferramentas:** Funções que fornecem aos LLMs recursos extras, como realizar cálculos ou acessar dados externos.

* **Como definir uma ferramenta:** Fornecendo uma descrição textual clara, entradas, saídas e uma função chamável.

* **Por que as ferramentas são essenciais**: Elas permitem que os agentes superem as limitações do treinamento de modelos estáticos, lidem com tarefas em tempo real e executem ações especializadas.

> As ferramentas desempenham um papel crucial no aprimoramento das capacidades dos agentes de IA.

## Questionário

P1: Qual das seguintes opções melhor descreve uma ferramenta de IA?
> Um processo executável ou API externa que permite que os agentes executem tarefas específicas e interajam com ambientes externos.

P2: Como os agentes de IA usam ferramentas como uma forma de "atuação" em um ambiente?
> Solicitando ao LLM que gere código de invocação de ferramentas quando apropriado e executando ferramentas em nome do modelo.

P3: O que é um Large Language Model (LLM)?

> Um modelo de aprendizado profundo treinado em grandes quantidades de texto para compreender e gerar linguagem semelhante à humana

P4: Qual das seguintes opções descreve melhor o papel de tokens especiais em LLMs?
> Eles desempenham funções específicas, como marcar o fim de uma sequência (EOS) ou separar diferentes papéis de mensagens em modelos de bate-papo

P5: Como os modelos de bate-papo com IA processam as mensagens do usuário internamente?
> Eles convertem as mensagens do usuário em um prompt formatado, concatenando mensagens do sistema, do usuário e do assistente