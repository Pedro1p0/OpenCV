import cv2
import numpy as np
import matplotlib.pyplot as plt

# Dimensões da imagem
width = 256
height = 256

# Amplitude da senoide
amplitude = 127

# Período da senoide
periods = 4

# Gerar a senoide
x = np.arange(width)
y = amplitude * np.sin(2 * np.pi * periods * x / width)

# Criar uma matriz 2D com a senoide
image = np.tile(y, (height, 1)).astype(np.uint8)

# Salvar a imagem em formato PNG
cv2.imwrite("senoide.png", image)

# Salvar a imagem em formato YML
file_storage = cv2.FileStorage("senoide.yml", cv2.FILE_STORAGE_WRITE)
file_storage.write("image", image)
file_storage.release()

# Ler a imagem salva em formato YML
file_storage = cv2.FileStorage("senoide.yml", cv2.FILE_STORAGE_READ)
loaded_image = file_storage.getNode("image").mat()
file_storage.release()

if loaded_image is None:
    print("Erro ao ler a imagem do arquivo YML.")
    exit()

# Extrair uma linha de cada imagem
line_index = 128
original_line = image[line_index]
loaded_line = loaded_image[line_index]

# Calcular a diferença entre as linhas
difference = np.abs(original_line.astype(int) - loaded_line.astype(int))

# Traçar o gráfico da diferença
plt.plot(difference)
plt.xlabel('Posição do pixel')
plt.ylabel('Diferença')
plt.title('Diferença entre as linhas das imagens')
plt.show()
