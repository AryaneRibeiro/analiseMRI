import streamlit as st
import cv2


def exibicaoResultados(imagem, imagem_processada, mascara=None):
    with st.container(border=True):
        col_original, col_processada, col_mascara = st.columns(3)

        # Coluna 1: Imagem Original
        with col_original:
            st.subheader("Imagem Original")
            with st.container(border=True, height=280):
                if imagem is not None:
                    st.image(imagem, use_container_width=True)
                else:
                    st.caption("A imagem aparecerá aqui após ser adicionada.")

        # Coluna 2: Após Processamento
        with col_processada:
            st.subheader("Após Processamento")
            with st.container(border=True, height=280):
                if imagem_processada is not None:
                    imagem_rgb = cv2.cvtColor(
                        imagem_processada,
                        cv2.COLOR_BGR2RGB
                    )
                    st.image(imagem_rgb, use_container_width=True)
                else:
                    st.caption("A imagem processada aparecerá aqui.")

        # Coluna 3: Máscara / Segmentação (Corrigido para exibir a variável mascara)
        with col_mascara:
            st.subheader("Segmentação")
            with st.container(border=True, height=280):
                if mascara is not None:
                    st.image(mascara, use_container_width=True)
                else:
                    st.caption("O tumor / máscara aparecerá aqui.")

        # Painel inferior de Classificação
        st.divider()
        st.subheader("Classificação")
        with st.container(border=True):
            st.write("O resultado da classificação aparecerá aqui.")
            st.caption("Após o processamento da imagem.")