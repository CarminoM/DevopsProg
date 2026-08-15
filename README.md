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
A aplicação mostra a resposta e a fonte utilizada