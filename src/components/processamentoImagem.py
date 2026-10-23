import streamlit as st

def processamentoImagem():
    with st.container(border=True):
            st.subheader("1. Adicionar Imagem")

            imagem = st.file_uploader(
                "Selecione uma imagem",
                type=["png", "jpg", "jpeg"],
                label_visibility="collapsed"
            )

            st.divider()

            st.subheader("2. Ajustes de Processamento")

            contraste = st.toggle("Aumento de contraste")
            ruido = st.toggle("Redução de ruído")

            st.divider()

            st.subheader("3. Ações")

            processar = st.button(
                "Processar",
                width="stretch",
                disabled=imagem is None
            )

            classificar = st.button(
                "Classificar",
                width="stretch",
                disabled=imagem is None
            )

            segmentar = st.button(
                "Segmentar",
                width="stretch",
                disabled=imagem is None
            )

    return imagem, contraste, ruido, processar, classificar, segmentar