import oci
import pandas as pd
import numpy as np


# --------------------------------------------------
# CONFIGURAÇÃO OCI
# --------------------------------------------------

import os
import streamlit as st

try:
    oci_secrets = st.secrets["oci"]

    config = {
        "user": oci_secrets["user"],
        "fingerprint": oci_secrets["fingerprint"],
        "tenancy": oci_secrets["tenancy"],
        "region": oci_secrets["region"],
        "key_content": oci_secrets["key_content"],
    }

    signer = oci.signer.Signer(
    tenancy=config["tenancy"],
    user=config["user"],
    fingerprint=config["fingerprint"],
    private_key_file_location=None,
    private_key_content=config["key_content"],
)

except Exception:
    config = oci.config.from_file()
    signer = None

endpoint = (
    "https://inference.generativeai."
    "sa-saopaulo-1.oci.oraclecloud.com"
)

if signer:
    cliente_ia = (
        oci.generative_ai_inference
        .GenerativeAiInferenceClient(
            config={},
            signer=signer,
            service_endpoint=endpoint,
            retry_strategy=oci.retry.NoneRetryStrategy(),
            timeout=(10, 240)
        )
    )
else:
    cliente_ia = (
        oci.generative_ai_inference
        .GenerativeAiInferenceClient(
            config=config,
            service_endpoint=endpoint,
            retry_strategy=oci.retry.NoneRetryStrategy(),
            timeout=(10, 240)
        )
    )


# --------------------------------------------------
# MODELOS
# --------------------------------------------------

MODEL_CHAT = "ocid1.generativeaimodel.oc1.sa-saopaulo-1.amaaaaaask7dceyaxu7lvx6k45r2hapxtuc2q5rleaujcowq6xbcywwtzhsq"
MODEL_EMBEDDING = "cohere.embed-v4.0"


# --------------------------------------------------
# BASE DE CONHECIMENTO
# --------------------------------------------------

base = pd.read_csv("base_conhecimento.csv")


# --------------------------------------------------
# GERAR EMBEDDING
# --------------------------------------------------

def gerar_embedding(texto, tipo_input):

    detalhes = (
        oci.generative_ai_inference.models
        .EmbedTextDetails()
    )

    detalhes.inputs = [texto]

    detalhes.serving_mode = (
        oci.generative_ai_inference.models
        .OnDemandServingMode(
            model_id=MODEL_EMBEDDING
        )
    )

    detalhes.compartment_id = config["tenancy"]

    detalhes.input_type = tipo_input

    resposta = cliente_ia.embed_text(detalhes)

    return resposta.data.embeddings[0]


# --------------------------------------------------
# CALCULAR SIMILARIDADE
# --------------------------------------------------

def calcular_similaridade(vetor1, vetor2):

    vetor1 = np.array(vetor1)
    vetor2 = np.array(vetor2)

    return np.dot(vetor1, vetor2) / (
        np.linalg.norm(vetor1)
        * np.linalg.norm(vetor2)
    )


# --------------------------------------------------
# GERAR EMBEDDINGS DA BASE
# --------------------------------------------------

def gerar_embeddings_base():

    embeddings = []

    for indice, linha in base.iterrows():

        texto = (
            f'{linha["tema"]}. '
            f'{linha["pergunta"]} '
            f'{linha["resposta"]}'
        )

        embedding = gerar_embedding(
            texto,
            "SEARCH_DOCUMENT"
        )

        embeddings.append(embedding)

    return embeddings


# --------------------------------------------------
# BUSCA SEMÂNTICA
# --------------------------------------------------

def buscar_conteudo(pergunta, embeddings_base):

    embedding_pergunta = gerar_embedding(
        pergunta,
        "SEARCH_QUERY"
    )

    melhor_indice = None
    maior_similaridade = -1

    for indice, embedding_base in enumerate(
        embeddings_base
    ):

        similaridade = calcular_similaridade(
            embedding_pergunta,
            embedding_base
        )

        if similaridade > maior_similaridade:

            maior_similaridade = similaridade
            melhor_indice = indice

    return (
        base.iloc[melhor_indice],
        maior_similaridade
    )


# --------------------------------------------------
# GERAR RESPOSTA COM IA
# --------------------------------------------------

def gerar_resposta(pergunta, contexto):

    prompt = f"""
Você é o DevopsProg.

Seu objetivo é ajudar pessoas iniciantes
a entender conceitos de programação.

Responda de maneira simples, clara e didática.

Use o conteúdo da base de conhecimento
como principal fonte da resposta.

Você pode dar exemplos simples para facilitar
o entendimento.

Se a pergunta não puder ser respondida com
o conteúdo fornecido, diga que não possui
informações suficientes.

CONTEÚDO DA BASE:

{contexto}

PERGUNTA DO USUÁRIO:

{pergunta}
"""

    chat_request = (
        oci.generative_ai_inference.models
        .CohereChatRequest()
    )

    chat_request.message = prompt
    chat_request.max_tokens = 500
    chat_request.temperature = 0.3

    chat_detail = (
        oci.generative_ai_inference.models
        .ChatDetails()
    )

    chat_detail.chat_request = chat_request

    chat_detail.serving_mode = (
        oci.generative_ai_inference.models
        .OnDemandServingMode(
            model_id=MODEL_CHAT
        )
    )

    chat_detail.compartment_id = config["tenancy"]

    response = cliente_ia.chat(chat_detail)

    return response.data.chat_response.text