import streamlit as st
import cv2 
import numpy as np

from components.cabecalho import mostrarCabecalho
from config.config import configurarPagina
from components.processamentoImagem import processamentoImagem
from components.resultado import exibicaoResultados

from tecnicas.ruido import reduzir_ruido
from tecnicas.contraste import aumentar_contraste
from tecnicas.segmentacao import segmentar_imagem

# Config da página 
configurarPagina()

if "imagem_processada" not in st.session_state:
    st.session_state.imagem_processada = None

if "mascara" not in st.session_state:
    st.session_state.mascara = None

# Cabeçalho (logo, título e sub-título)
mostrarCabecalho()

# Carregar imagem, processar, classificar e segmentar
col_lateral, col_resultados = st.columns(
    [1, 2.5],
    gap="medium"
)

with col_lateral:
    (
        imagem,
        contraste,
        ruido,
        processar,
        classificar,
        segmentar
    ) = processamentoImagem()


imagem_processada = None


# Processar somente quando o botão for clicado
if processar and imagem is not None:
    bytes_imagem = np.frombuffer(
        imagem.getvalue(),
        dtype=np.uint8
    )

    imagem_cv = cv2.imdecode(
        bytes_imagem,
        cv2.IMREAD_COLOR
    )

    if imagem_cv is not None:
        resultado = imagem_cv.copy()

        if ruido:
            resultado = reduzir_ruido(resultado)

        if contraste:
            resultado = aumentar_contraste(resultado)

        # Guarda a imagem processada na sessão
        st.session_state.imagem_processada = resultado

        # Limpa a máscara antiga
        st.session_state.mascara = None


# Painel de resultados
with col_resultados:
    exibicaoResultados(
        imagem,
        st.session_state.imagem_processada
    )