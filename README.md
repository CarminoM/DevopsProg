# DevopsProg

O **DevopsProg** é um assistente inteligente criado para ajudar pessoas iniciantes a entender conceitos de programação de forma simples, clara e didática.

O projeto foi desenvolvido como parte de um challenge da Alura em parceria com a Oracle, utilizando recursos de Inteligência Artificial da **Oracle Cloud Infrastructure (OCI)**.

---

## Objetivo do projeto

O objetivo do DevopsProg é permitir que uma pessoa faça perguntas em linguagem natural sobre programação e receba respostas didáticas baseadas em uma base de conhecimento própria.

Exemplos de perguntas:

* O que é uma API?
* O que faz um Service?
* Qual componente fala com o banco de dados?
* O que é uma classe?
* Para que serve o GitHub?

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
A aplicação mostra a resposta e a fonte utilizada
```

---

## Busca semântica

O DevopsProg não depende apenas de palavras iguais.

Por exemplo, a pergunta:

```text
Qual componente fala com o banco de dados?
```

consegue encontrar o conteúdo relacionado a:

```text
Repository
```

mesmo que a palavra `Repository` não apareça na pergunta.

Isso é possível utilizando embeddings e comparação por similaridade.

---

## Base de conhecimento

A base de conhecimento está armazenada no arquivo:

```text
base_conhecimento.csv
```

Atualmente ela possui conteúdos sobre:

* Java
* Spring Boot
* APIs
* Git
* GitHub
* Banco de dados

Cada registro possui os seguintes campos:

```text
categoria
tema
pergunta
resposta
```

---

## Inteligência Artificial

O projeto utiliza serviços da Oracle Cloud Infrastructure.

### OCI Generative AI

Responsável por gerar respostas em linguagem natural a partir da pergunta do usuário e do conteúdo encontrado na base de conhecimento.

### OCI Embeddings

Responsável por transformar perguntas e conteúdos da base em representações numéricas.

Modelo de embedding utilizado:

```text
cohere.embed-v4.0
```

A busca utiliza similaridade de cosseno para encontrar o conteúdo semanticamente mais próximo da pergunta do usuário.

---

## Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* NumPy
* Oracle Cloud Infrastructure (OCI)
* OCI Generative AI
* OCI Embeddings
* Cohere
* OCI Python SDK
* Git
* GitHub

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
```

---

## Função dos principais arquivos

### app.py

Responsável pela interface da aplicação utilizando Streamlit.

Também controla:

* campo de perguntas;
* histórico da conversa;
* exibição das respostas;
* exibição das fontes.

### ia_service.py

Responsável pela lógica de Inteligência Artificial.

Ele realiza:

* conexão com a Oracle Cloud;
* geração de embeddings;
* busca semântica;
* cálculo de similaridade;
* envio da pergunta para o modelo de IA;
* retorno da resposta.

### base_conhecimento.csv

Contém os conteúdos utilizados como base de conhecimento do agente.

---

## Segurança

Informações sensíveis não são enviadas para o GitHub.

O arquivo:

```text
.env
```

é ignorado através do:

```text
.gitignore
```

As credenciais utilizadas para autenticação na Oracle Cloud também são mantidas fora do repositório.

---

## Como executar localmente

### 1. Clone o projeto

```bash
git clone https://github.com/CarminoM/DevopsProg.git
```

### 2. Entre na pasta do projeto

```bash
cd DevopsProg
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configure a autenticação da OCI

É necessário possuir uma conta Oracle Cloud e configurar o arquivo:

```text
~/.oci/config
```

com as credenciais necessárias para acessar os serviços utilizados pelo projeto.

### 5. Execute a aplicação

```bash
python -m streamlit run app.py
```

A aplicação será aberta no navegador.

---

## Exemplos de funcionamento

### Pergunta sobre API

```text
O que é uma API?
```

O DevopsProg consulta a base de conhecimento e utiliza o OCI Generative AI para gerar uma explicação didática.

### Pergunta usando significado

```text
Qual componente fala com o banco de dados?
```

A busca semântica identifica que o conteúdo mais relacionado é:

```text
Repository
```

mesmo que a palavra `Repository` não apareça na pergunta.

### Pergunta fora da base

```text
Como funciona a fotossíntese?
```

Nesse caso, o sistema informa que não encontrou informações suficientes na base de conhecimento.

---

## Limitações atuais

A versão atual possui algumas limitações:

* base de conhecimento ainda pequena;
* conteúdos armazenados apenas em CSV;
* não possui autenticação de usuários;
* não utiliza banco vetorial;
* a qualidade das respostas depende da qualidade da base de conhecimento.

---

## Melhorias futuras

Possíveis evoluções do DevopsProg:

* adicionar documentos em PDF à base de conhecimento;
* aumentar a quantidade de conteúdos disponíveis;
* implementar banco vetorial;
* evoluir para uma arquitetura RAG mais completa;
* melhorar o histórico da conversa;
* adicionar avaliação da qualidade das respostas;
* personalizar melhor a interface;

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

```
---

## Deploy

A aplicação está publicada no **Streamlit Community Cloud** e integrada aos serviços de Inteligência Artificial da Oracle Cloud Infrastructure.

O deploy utiliza:

- código-fonte hospedado no GitHub;
- Streamlit Community Cloud para execução da aplicação;
- Secrets do Streamlit para armazenamento seguro das credenciais;
- OCI Generative AI para geração das respostas;
- OCI Embeddings para busca semântica.

### Aplicação online

https://carminom-devopsprog-app-yoyqhw.streamlit.app/

---

## Status do projeto

Versão funcional publicada em ambiente cloud.

Atualmente o projeto já possui:

* interface web com Streamlit;
* histórico de conversa;
* base de conhecimento própria em CSV;
* busca semântica;
* integração com Oracle Cloud Infrastructure;
* uso de embeddings;
* respostas geradas por Inteligência Artificial;
* identificação da fonte utilizada;
* exibição da similaridade da busca;
* tratamento de perguntas fora do escopo.
* deploy realizado no Streamlit Community Cloud;
* aplicação disponível por link público;

---

---

## Evidências do projeto

O projeto foi validado com diferentes tipos de perguntas.

### Busca semântica

Pergunta:

```text
Qual componente fala com o banco de dados?

Resultado identificado pela busca:
Repository

Pergunta fora do escopo

Pergunta:

Como funciona a fotossíntese?

Resultado:

O DevopsProg informa que não encontrou informações suficientes na base de conhecimento.

Integração com IA

As respostas são geradas pelo OCI Generative AI utilizando como contexto o conteúdo recuperado da base de conhecimento.

---

## Autoria

Projeto desenvolvido por **Carmino Massi** como parte de um challenge da Alura em parceria com a Oracle.