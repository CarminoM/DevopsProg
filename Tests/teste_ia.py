import oci

# Carrega sua configuração da OCI
config = oci.config.from_file()

# Endpoint da região de São Paulo
endpoint = "https://inference.generativeai.sa-saopaulo-1.oci.oraclecloud.com"

# Cria o cliente do Generative AI
generative_ai_inference_client = (
    oci.generative_ai_inference.GenerativeAiInferenceClient(
        config=config,
        service_endpoint=endpoint,
        retry_strategy=oci.retry.NoneRetryStrategy(),
        timeout=(10, 240)
    )
)

# Cria os detalhes da conversa
chat_detail = oci.generative_ai_inference.models.ChatDetails()

# Cria a pergunta para o modelo Cohere
chat_request = oci.generative_ai_inference.models.CohereChatRequest()

chat_request.message = (
    "Explique o que é uma API REST como se eu fosse iniciante em programação."
)

chat_request.max_tokens = 500
chat_request.temperature = 0.3

chat_detail.chat_request = chat_request

# COLE AQUI O MODEL_ID QUE A ORACLE MOSTROU
chat_detail.serving_mode = (
    oci.generative_ai_inference.models.OnDemandServingMode(
        model_id="ocid1.generativeaimodel.oc1.sa-saopaulo-1.amaaaaaask7dceyaxu7lvx6k45r2hapxtuc2q5rleaujcowq6xbcywwtzhsq")
    )


# Seu compartment
chat_detail.compartment_id = config["tenancy"]

# Envia a pergunta
response = generative_ai_inference_client.chat(chat_detail)

# Mostra a resposta completa
print("\nResposta da IA:\n")
print(response.data.chat_response.text)