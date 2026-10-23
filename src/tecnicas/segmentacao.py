import cv2

def segmentar_imagem(imagem):
    # Converte a imagem colorida para tons de cinza
    imagem_cinza = cv2.cvtColor(
        imagem,
        cv2.COLOR_BGR2GRAY
    )

    # Aplica um desfoque leve para reduzir pequenas variações
    imagem_suave = cv2.GaussianBlur(
        imagem_cinza,
        (5, 5),
        0
    )

    # Segmenta a imagem usando o método de Otsu
    _, mascara = cv2.threshold(
        imagem_suave,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return mascara
