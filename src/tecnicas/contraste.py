import cv2

def aumentar_contraste(imagem):
    lab = cv2.cvtColor(
        imagem,
        cv2.COLOR_BGR2LAB
    )

    luminancia, canal_a, canal_b = cv2.split(lab)

    luminancia = cv2.equalizeHist(luminancia)

    lab = cv2.merge(
        (luminancia, canal_a, canal_b)
    )

    return cv2.cvtColor(
        lab,
        cv2.COLOR_LAB2BGR
    )