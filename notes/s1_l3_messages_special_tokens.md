# Mensagens e Tokens Especiais

source: [HF:messages-and-special-tokens](https://huggingface.co/learn/agents-course/unit1/messages-and-special-tokens)

### Compreendendo os Modelos de Chat

Como cada **modelo de instrução** utiliza diferentes `formatos de conversação` e `tokens especiais`, os **modelos de chat** são implementados para garantir que formatemos o prompt corretamente, conforme esperado por cada modelo.

Em **transformers**, os `modelos de chat` incluem código `Jinja2` que descreve como transformar a **lista de mensagens JSON do ChatML**, conforme apresentado nos exemplos acima, em uma representação textual das instruções em 
nível de sistema, 
mensagens do usuário e 
respostas do assistente que o modelo pode entender.

Essa estrutura ajuda a manter a consistência entre as interações e garante que o modelo responda adequadamente a diferentes tipos de entradas.


### Mensagens para Prompts

A maneira mais fácil de garantir que seu LLM receba uma conversa formatada corretamente é usar o `chat_template` do `tokenizador` do modelo.

```python
messages = [
    {"role": "system", "content": "You are an AI assistant with access to various tools."},
    {"role": "user", "content": "Hi !"},
    {"role": "assistant", "content": "Hi human, what can help you with ?"},
]
```

Para converter a conversa anterior em um `prompt`, carregue o `tokenizador` e chame `apply_chat_template`:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)      
```
O `rendered_prompt` retornado por esta função agora está pronto para ser usado como entrada para o modelo que você escolheu!

Esta função `apply_chat_template()` será usada no backend da sua API quando você interagir com mensagens no formato `ChatML`.

Agora que vimos como os LLMs estruturam suas entradas por meio de `modelos de chat`, vamos explorar como os `Agentes` agem em seus ambientes.

Uma das principais maneiras de fazer isso é usando `Ferramentas`, que __**estendem os recursos**__ de um modelo de IA para além da geração de texto.

