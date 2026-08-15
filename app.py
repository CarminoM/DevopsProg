import streamlit as st

from ia_service import (
    gerar_embeddings_base,
    buscar_conteudo,
    gerar_resposta
)


# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="DevopsProg",
    page_icon="🤖"
)

st.title("🤖 DevopsProg")

st.write(
    "Assistente inteligente para ajudar iniciantes "
    "a entender conceitos de programação."
)

st.divider()


# --------------------------------------------------
# CARREGA EMBEDDINGS UMA ÚNICA VEZ
# --------------------------------------------------

@st.cache_resource
def carregar_embeddings():
    return gerar_embeddings_base()


embeddings_base = carregar_embeddings()


# --------------------------------------------------
# HISTÓRICO
# --------------------------------------------------

if "mensagens" not in st.session_state:

    st.session_state.mensagens = []


for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["tipo"]):

        st.write(mensagem["conteudo"])

        if "fonte" in mensagem:
            st.caption(mensagem["fonte"])


# --------------------------------------------------
# CAMPO DE PERGUNTA
# --------------------------------------------------

pergunta_usuario = st.chat_input(
    "Digite sua pergunta sobre programação..."
)


if pergunta_usuario:

    st.session_state.mensagens.append(
        {
            "tipo": "user",
            "conteudo": pergunta_usuario
        }
    )

    with st.chat_message("user"):
        st.write(pergunta_usuario)

    try:

        resultado, similaridade = buscar_conteudo(
            pergunta_usuario,
            embeddings_base
        )

        if similaridade >= 0.25:

            contexto = resultado["resposta"]

            resposta_ia = gerar_resposta(
                pergunta_usuario,
                contexto
            )

            fonte = (
                f'Fonte: base_conhecimento.csv | '
                f'Categoria: {resultado["categoria"]} | '
                f'Tema: {resultado["tema"]} | '
                f'Similaridade: {similaridade:.2f}'
            )

            st.session_state.mensagens.append(
                {
                    "tipo": "assistant",
                    "conteudo": resposta_ia,
                    "fonte": fonte
                }
            )

            with st.chat_message("assistant"):

                st.write(resposta_ia)

                st.caption(fonte)

        else:

            resposta = (
                "Não encontrei informações suficientes "
                "sobre esse assunto na minha base de conhecimento."
            )

            st.session_state.mensagens.append(
                {
                    "tipo": "assistant",
                    "conteudo": resposta
                }
            )

            with st.chat_message("assistant"):
                st.write(resposta)

    except Exception as erro:

        with st.chat_message("assistant"):

            st.error(
                "Ocorreu um erro ao consultar "
                "a inteligência artificial."
            )

            st.write(erro)