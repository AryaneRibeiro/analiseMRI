import streamlit as st

logo_caminho = "assets/icons/logo.png"

def mostrarCabecalho():
    col_logo, col_texto = st.columns([1, 8], vertical_alignment="center")

    with col_logo:
        st.image(logo_caminho, width=100)

    with col_texto:
        st.title("Análise de tumores cerebrais")
        st.markdown(
            "Sistema de processamento e análise de imagens médicas"
        )

    st.divider()