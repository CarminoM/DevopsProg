import oci
import numpy as np

# Carrega sua configuração da OCI
config = oci.config.from_file()

# Endpoint da região de São Paulo
endpoint = (
    "https://inference.generativeai."
    "sa-saopaulo-1.oci.oraclecloud.com"
)

# Cria o cliente da IA
cliente = (
    oci.generative_ai_inference
    .GenerativeAiInferenceClient(
        config=config,
        service_endpoint=endpoint,
        retry_strategy=oci.retry.NoneRetryStrategy(),
        timeout=(10, 240)
    )
)

# Modelo de embedding
MODEL_ID = "cohere.embed-v4.0"

# Função que transforma texto em números
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


# Texto da nossa base
texto_base = (
    "Repository é responsável pela comunicação "
    "com o banco de dados."
)

# Pergunta do usuário
pergunta = (
    "Qual componente fala com o banco de dados?"
)

# Gera os embeddings
embedding_base = gerar_embedding(
    texto_base,
    "SEARCH_DOCUMENT"
)

embedding_pergunta = gerar_embedding(
    pergunta,
    "SEARCH_QUERY"
)

# Calcula similaridade de cosseno
vetor_base = np.array(embedding_base)
vetor_pergunta = np.array(embedding_pergunta)

similaridade = np.dot(
    vetor_base,
    vetor_pergunta
) / (
    np.linalg.norm(vetor_base)
    * np.linalg.norm(vetor_pergunta)
)

print("Texto da base:")
print(texto_base)

print("\nPergunta:")
print(pergunta)

print("\nSimilaridade:")
print(similaridade)