import cv2
import numpy as np
import matplotlib.pyplot as plt
import ctypes

def swap_quadrants(image):
    tmp = np.copy(image)
    cx = image.shape[1] // 2
    cy = image.shape[0] // 2
    image[:cy, :cx] = tmp[cy:, cx:]
    image[:cy, cx:] = tmp[cy:, :cx]
    image[cy:, :cx] = tmp[:cy, cx:]
    image[cy:, cx:] = tmp[:cy, :cx]

def calculate_magnitude_spectrum(image):
    # Realiza a DFT
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # Calcula o espectro de magnitude
    magnitude_spectrum = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

    # Normaliza a faixa de valores para [0, 1]
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 1, cv2.NORM_MINMAX)

    return magnitude_spectrum

def main():
    # Carrega a imagem em escala de cinza
    image = cv2.imread("/home/bolsistaspop/pedro-vitor/opencv/ex9/Figura7.png", cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao abrir a imagem.")
        return

    # Carrega a biblioteca libGL.so.1
    ctypes.cdll.LoadLibrary('libGL.so.1')

    # Calcula o espectro de magnitude
    magnitude_spectrum = calculate_magnitude_spectrum(image)

    # Exibe a imagem original e o espectro de magnitude
    cv2.imshow("Imagem", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Plota o espectro de magnitude usando matplotlib
    plt.figure(figsize=(8, 6))
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
