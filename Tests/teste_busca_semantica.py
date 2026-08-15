import oci
import pandas as pd
import numpy as np

# Carrega configuração OCI
config = oci.config.from_file()

endpoint = (
    "https://inference.generativeai."
    "sa-saopaulo-1.oci.oraclecloud.com"
)

cliente = (
    oci.generative_ai_inference
    .GenerativeAiInferenceClient(
        config=config,
        service_endpoint=endpoint,
        retry_strategy=oci.retry.NoneRetryStrategy(),
        timeout=(10, 240)
    )
)

MODEL_ID = "cohere.embed-v4.0"

# Carrega nosso CSV
base = pd.read_csv("base_conhecimento.csv")


def gerar_embedding(texto, tipo_input):

    detalhes = (
        oci.generative_ai_inference.models
        .EmbedTextDetails()
    )

    detalhes.inputs = [texto]

    detalhes.serving_mode = (
        oci.generative_ai_inference.models
        .OnDemandServingMode(
            model_id=MODEL_ID
        )
    )

    detalhes.compartment_id = config["tenancy"]

    detalhes.input_type = tipo_input

    resposta = cliente.embed_text(detalhes)

    return resposta.data.embeddings[0]


def calcular_similaridade(vetor1, vetor2):

    vetor1 = np.array(vetor1)
    vetor2 = np.array(vetor2)

    return np.dot(vetor1, vetor2) / (
        np.linalg.norm(vetor1)
        * np.linalg.norm(vetor2)
    )


# Pergunta que antes dava problema
pergunta = "Qual componente fala com o banco de dados?"

embedding_pergunta = gerar_embedding(
    pergunta,
    "SEARCH_QUERY"
)

resultados = []

for indice, linha in base.iterrows():

    texto_base = (
        f'{linha["tema"]}. '
        f'{linha["pergunta"]} '
        f'{linha["resposta"]}'
    )

    embedding_base = gerar_embedding(
        texto_base,
        "SEARCH_DOCUMENT"
    )

    similaridade = calcular_similaridade(
        embedding_pergunta,
        embedding_base
    )

    resultados.append(
        {
            "tema": linha["tema"],
            "categoria": linha["categoria"],
            "similaridade": similaridade
        }
    )

# Ordena do mais parecido para o menos parecido
resultados = sorted(
    resultados,
    key=lambda x: x["similaridade"],
    reverse=True
)

print("\nPergunta:")
print(pergunta)

print("\nResultados mais relacionados:\n")

for resultado in resultados:

    print(
        resultado["tema"],
        "-",
        round(resultado["similaridade"], 4)
    )