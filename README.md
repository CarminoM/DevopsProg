# DevopsProg

O **DevopsProg** é um assistente inteligente criado para ajudar pessoas iniciantes a entender conceitos de programação de forma simples, clara e didática.

O projeto foi desenvolvido como parte de um challenge da Alura em parceria com a Oracle, utilizando recursos de Inteligência Artificial da **Oracle Cloud Infrastructure (OCI)**.

---

## Objetivo do projeto

O objetivo do DevopsProg é permitir que uma pessoa faça perguntas em linguagem natural sobre programação e receba respostas didáticas baseadas em uma base de conhecimento própria.

Exemplos de perguntas:

- O que é uma API?
- O que faz um Service?
- Qual componente fala com o banco de dados?
- O que é uma classe?
- Para que serve o GitHub?

---

## Como funciona

O fluxo da aplicação é:

```text
Usuário faz uma pergunta
        ↓
A pergunta é transformada em embedding
        ↓
A aplicação compara o significado da pergunta
com os conteúdos da base CSV
        ↓
O conteúdo mais relacionado é selecionado
        ↓
Esse conteúdo é enviado para o OCI Generative AI
        ↓
A IA gera uma resposta didática
        ↓
A aplicação mostra a resposta e a fonte utiliza


---

## Busca semântica

O DevopsProg não depende apenas de palavras iguais.

Por exemplo, a pergunta:

```text
Qual componente fala com o banco de dados?
Repository

---

## Base de conhecimento

A base de conhecimento está armazenada no arquivo:

```text
base_conhecimento.csv

categoria
tema
pergunta
resposta

---

## Inteligência Artificial

O projeto utiliza serviços da Oracle Cloud Infrastructure.

### OCI Generative AI

Responsável por gerar respostas em linguagem natural.

### OCI Embeddings

Responsável por transformar perguntas e conteúdos da base em representações numéricas.

Modelo de embedding utilizado:

```text
cohere.embed-v4.0

---

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- Oracle Cloud Infrastructure (OCI)
- OCI Generative AI
- OCI Embeddings
- Cohere
- OCI Python SDK
- Git
- GitHub

---

## Estrutura do projeto

```text
DevopsProg/
│
├── Tests/
│   ├── teste_busca_semantica.py
│   ├── teste_embedding.py
│   ├── teste_ia.py
│   └── teste_oci.py
│
├── app.py
├── ia_service.py
├── base_conhecimento.csv
├── requirements.txt
├── .gitignore
└── README.md

---

## Função dos principais arquivos

### app.py

Responsável pela interface da aplicação utilizando Streamlit.

Também controla:

- campo de perguntas;
- histórico da conversa;
- exibição das respostas;
- exibição das fontes.

### ia_service.py

Responsável pela lógica de Inteligência Artificial.

Ele realiza:

- conexão com a Oracle Cloud;
- geração de embeddings;
- busca semântica;
- cálculo de similaridade;
- envio da pergunta para o modelo de IA;
- retorno da resposta.

### base_conhecimento.csv

Contém os conteúdos utilizados como base de conhecimento do agente.

---

## Segurança

Informações sensíveis não são enviadas para o GitHub.

O arquivo:

```text
.env

.gitignore

---

## Como executar localmente

### 1. Clone o projeto

```bash
git clone https://github.com/CarminoM/DevopsProg.git

---

## Exemplos de funcionamento

### Pergunta sobre API

```text
O que é uma API?

Qual componente fala com o banco de dados?

Repository

Como funciona a fotossíntese?
Nesse caso, o sistema informa que não encontrou informações suficientes na base de conhecimento.

---

## Limitações atuais

A versão atual possui algumas limitações:

- base de conhecimento ainda pequena;
- conteúdos armazenados apenas em CSV;
- não possui autenticação de usuários;
- não utiliza banco vetorial;
- ainda não possui deploy publicado em nuvem;
- a qualidade das respostas depende da qualidade da base de conhecimento.

---

## Melhorias futuras

Possíveis evoluções do DevopsProg:

- adicionar documentos em PDF à base de conhecimento;
- aumentar a quantidade de conteúdos disponíveis;
- implementar banco vetorial;
- evoluir para uma arquitetura RAG mais completa;
- melhorar o histórico da conversa;
- adicionar avaliação da qualidade das respostas;
- personalizar melhor a interface;
- realizar o deploy da aplicação em ambiente cloud.

---

## Arquitetura simplificada

```text
Usuário
   ↓
Streamlit
   ↓
Pergunta em linguagem natural
   ↓
OCI Embeddings
   ↓
Busca semântica no CSV
   ↓
Conteúdo mais relacionado
   ↓
OCI Generative AI
   ↓
Resposta didática
   ↓
Fonte + categoria + tema + similaridade

---

## Status do projeto

Versão funcional em ambiente local.

Atualmente o projeto já possui:

- interface web com Streamlit;
- histórico de conversa;
- base de conhecimento própria em CSV;
- busca semântica;
- integração com Oracle Cloud Infrastructure;
- uso de embeddings;
- respostas geradas por Inteligência Artificial;
- identificação da fonte utilizada;
- exibição da similaridade da busca;
- tratamento de perguntas fora do escopo.

---

## Autoria

Projeto desenvolvido por **Carmino Massi** como parte de um challenge da Alura em parceria com a Oracle.