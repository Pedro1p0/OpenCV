import cv2
import numpy as np
import yaml
import matplotlib.pyplot as plt

SIDE = 256
PERIODOS = 8

def calculate_magnitude_spectrum(image):
    # Realiza a DFT
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # Calcula o espectro de magnitude
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    # Normaliza a faixa de valores para [0, 1]
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 1, cv2.NORM_MINMAX)

    return magnitude_spectrum

# Carrega os dados do arquivo YAML
with open("senoide-256.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.SafeLoader)

image = np.array(data["mat"], dtype=np.float32)

# Calcula o espectro de magnitude
magnitude_spectrum = calculate_magnitude_spectrum(image)

# Exibe a imagem original e o espectro de magnitude
plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.axis("off")
plt.title("Imagem Original")

plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.axis("off")
plt.title("Espectro de Magnitude")

plt.tight_layout()
plt.show()
