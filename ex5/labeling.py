import cv2
import sys

def main():
    # Verifica se foi passado o caminho da imagem como argumento
    if len(sys.argv) < 2:
        print("Uso: python labeling.py <imagem>")
        return

    # Carrega a imagem em escala de cinza
    image_path = sys.argv[1]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao carregar a imagem.")
        return

    # Obtém as dimensões da imagem
    width = image.shape[1]
    height = image.shape[0]
    print(f"Tamanho da imagem: {width}x{height}")

    # Define um ponto de referência inicial para o flood fill
    reference_point = (0, 0)

    # Executa o flood fill nas bordas da imagem
    for i in range(height):
        if image[i, width - 1] == 255:
            reference_point = (width - 1, i)
            cv2.floodFill(image, None, reference_point, 0)
        if image[i, 0] == 255:
            reference_point = (0, i)
            cv2.floodFill(image, None, reference_point, 0)

    for j in range(width):
        if image[height - 1, j] == 255:
            reference_point = (j, height - 1)
            cv2.floodFill(image, None, reference_point, 0)
        if image[0, j] == 255:
            reference_point = (j, 0)
            cv2.floodFill(image, None, reference_point, 0)

    # Conta os objetos presentes na imagem
    num_objects = 0
    for i in range(height):
        for j in range(width):
            if image[i, j] == 255:
                # Encontrou um objeto
                num_objects += 1
                # Inicia o flood fill a partir das coordenadas (i, j)
                # Preenche o objeto com o número do objeto
                cv2.floodFill(image, None, (j, i), num_objects)

    # Encontra os contornos dos objetos
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Conta os objetos com furos
    num_objects_with_holes = 0
    for i in range(len(contours)):
        if hierarchy[0, i, 3] == -1:
            # O contorno não possui contornos internos
            # Verifica se há contornos externos para determinar se há um furo
            has_external_contour = hierarchy[0, i, 2] != -1
            if has_external_contour:
                # O objeto tem um furo
                num_objects_with_holes += 1

    # Exibe o resultado
    print(f"A figura tem {num_objects} objetos, {num_objects_with_holes} com furos e {num_objects - num_objects_with_holes} sem furos")
    cv2.imshow("Imagem", image)
    cv2.imwrite("labeling.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
