import cv2

def reduzir_ruido(imagem):
    return cv2.GaussianBlur(
        imagem,
        (5, 5),
        0
    )