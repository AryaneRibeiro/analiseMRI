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

# Configuração da página
configurarPagina()

# Inicialização do estado da sessão (Session State)
if "imagem_processada" not in st.session_state:
    st.session_state.imagem_processada = None

if "mascara" not in st.session_state:
    st.session_state.mascara = None

# Cabeçalho (logo, título e subtítulo)
mostrarCabecalho()

# Layout de colunas principais (Painel Lateral vs. Resultados)
col_lateral, col_resultados = st.columns(
    [1, 2.5],
    gap="medium"
)

# Painel lateral com controles e upload
with col_lateral:
    (
        imagem,
        contraste,
        ruido,
        processar,
        classificar,
        segmentar
    ) = processamentoImagem()

# Lógica de Processamento da Imagem
if processar and imagem is not None:
    bytes_imagem = np.frombuffer(imagem.getvalue(), dtype=np.uint8)
    imagem_cv = cv2.imdecode(bytes_imagem, cv2.IMREAD_COLOR)

    if imagem_cv is not None:
        resultado = imagem_cv.copy()

        if ruido:
            resultado = reduzir_ruido(resultado)

        if contraste:
            resultado = aumentar_contraste(resultado)

        # Atualiza a sessão com a imagem processada e reseta a máscara antiga
        st.session_state.imagem_processada = resultado
        st.session_state.mascara = None

# Lógica de Segmentação da Imagem
if segmentar and imagem is not None:
    # Prioriza usar a imagem já processada; se não existir, usa a original
    if st.session_state.imagem_processada is not None:
        base_imagem = st.session_state.imagem_processada
    else:
        bytes_imagem = np.frombuffer(imagem.getvalue(), dtype=np.uint8)
        base_imagem = cv2.imdecode(bytes_imagem, cv2.IMREAD_COLOR)

    if base_imagem is not None:
        st.session_state.mascara = segmentar_imagem(base_imagem)

# Renderização do Painel de Resultados
with col_resultados:
    exibicaoResultados(
        imagem,
        st.session_state.imagem_processada,
        st.session_state.mascara
    )