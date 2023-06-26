import cv2

# Carregar a imagem
image = cv2.imread('dom_pedro.jpg')

# Verificar se a imagem foi carregada corretamente
if image is None:
    print("Erro ao carregar a imagem.")
    exit()

# Obter as dimensões da imagem
altura, largura, _ = image.shape

# Solicitar ao usuário as coordenadas dos pontos P1 e P2
x1 = int(input("Digite a coordenada x de P1: "))
y1 = int(input("Digite a coordenada y de P1: "))
x2 = int(input("Digite a coordenada x de P2: "))
y2 = int(input("Digite a coordenada y de P2: "))

# Verificar se as coordenadas estão dentro dos limites da imagem
if x1 < 0 or x1 >= altura or y1 < 0 or y1 >= largura or x2 < 0 or x2 >= altura or y2 < 0 or y2 >= largura:
    print("Coordenadas inválidas.")
    exit()

# Criar uma cópia da imagem para exibir o resultado
result = image.copy()

# Converter a região definida pelo retângulo em negativo
result[x1:x2, y1:y2] = 255 - result[x1:x2, y1:y2]

# Exibir a imagem original e o resultado
cv2.imshow('Imagem Original', image)
cv2.imshow('Resultado', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
