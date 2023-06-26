import cv2
import numpy as np

def generate_dots_image(image, edges, dot_size):
    dots_image = np.zeros_like(image)

    # Desenhar pontos grandes na imagem pontilhista básica
    dots_image[edges] = 255

    # Usar a posição dos pixels de borda encontrados pelo algoritmo de Canny
    # para desenhar pontos nos respectivos locais na imagem gerada
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if edges[y, x] > 0:
                cv2.circle(dots_image, (x, y), dot_size, (255), -1)

    return dots_image

if __name__ == '__main__':
    # Carregar a imagem
    image = cv2.imread('/home/bolsistaspop/pedro-vitor/opencv/ex11/cafe.jpeg', cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao abrir a imagem.")
        exit()

    # Aplicar o algoritmo de Canny para obter as bordas
    edges = cv2.Canny(image, 100, 200)

    # Gerar a imagem pontilhista utilizando as bordas
    dot_size = 3  # Tamanho dos pontos a serem desenhados
    dots_image = generate_dots_image(image, edges, dot_size)

    # Exibir as imagens
    cv2.imshow("Imagem Original", image)
    cv2.imshow("Bordas (Canny)", edges)
    cv2.imshow("Imagem Pontilhista", dots_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
