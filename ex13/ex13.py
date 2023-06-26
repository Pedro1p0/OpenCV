import cv2
import numpy as np

def apply_morphological_operations(image):
    # Define o elemento estruturante
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Dilatação
    dilated = cv2.dilate(image, element)

    # Erosão
    eroded = cv2.erode(dilated, element)

    # Fechamento
    closing = cv2.morphologyEx(eroded, cv2.MORPH_CLOSE, element)

    # Abertura
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, element)

    # Abertura seguida de fechamento
    opened_closed = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, element)

    # Concatena as imagens em uma única linha
    images = np.hstack((dilated, eroded, closing, opening, opened_closed))

    return images

# Carrega as imagens de teste
test_images = ['ex13/digitos-1.png', 'ex13/digitos-2.png', 'ex13/digitos-3.png', 'ex13/digitos-4.png', 'ex13/digitos-5.png']

for image_path in test_images:
    # Carrega a imagem
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        continue

    # Aplica a pré-filtragem
    filtered_image = apply_morphological_operations(image)

    # Exibe a imagem original e a imagem pré-filtrada
    cv2.imshow("Imagem Original", image)
    cv2.imshow("Imagem Pré-filtrada", filtered_image)

    cv2.waitKey(0)

cv2.destroyAllWindows()
