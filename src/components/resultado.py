import streamlit as st
import cv2


def exibicaoResultados(imagem, imagem_processada):
    with st.container(border=True):
        col_original, col_processada, col_mascara = st.columns(3)

        with col_original:
            st.subheader("Imagem Original")

            with st.container(border=True, height=280):
                if imagem is not None:
                    st.image(imagem, width="stretch")
                else:
                    st.caption(
                        "A imagem aparecerá aqui após ser adicionada."
                    )

        with col_processada:
            st.subheader("Após Processamento")

            with st.container(border=True, height=280):
                if imagem_processada is not None:
                    # OpenCV usa BGR; Streamlit deve receber RGB
                    imagem_rgb = cv2.cvtColor(
                        imagem_processada,
                        cv2.COLOR_BGR2RGB
                    )
                    st.image(imagem_rgb, width="stretch")
                else:
                    st.caption("A imagem processada aparecerá aqui.")

        with col_mascara:
            st.subheader("Segmentação")

            with st.container(border=True, height=280):
                st.caption("A máscara aparecerá aqui.")

        st.divider()
        st.subheader("Classificação")

        with st.container(border=True):
            st.write(
                "O resultado da classificação aparecerá aqui."
            )
            st.caption("Após o processamento da imagem.")
