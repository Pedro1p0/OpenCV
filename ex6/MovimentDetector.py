import cv2

# Função de comparação de histogramas (pode ser substituída por outra, se desejado)
def compare_histograms(hist1, hist2):
    # Calcula a diferença entre os histogramas usando a distância de Bhattacharyya
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)

def main():
    # Inicializa a captura de vídeo
    cap = cv2.VideoCapture(0)  # Use o índice correto se tiver várias câmeras conectadas

    if not cap.isOpened():
        print("Não foi possível abrir a câmera")
        return

    # Obtém o primeiro frame e calcula seu histograma
    ret, frame = cap.read()
    prev_hist = cv2.calcHist([frame], [0], None, [256], [0, 256])
    prev_hist = cv2.normalize(prev_hist, prev_hist, 0, 1, cv2.NORM_MINMAX)

    # Limiar para detecção de movimento
    threshold = 0.5

    while True:
        # Lê o próximo frame
        ret, frame = cap.read()

        if not ret:
            print("Não foi possível ler o próximo frame")
            break

        # Converte o frame para tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calcula o histograma do frame atual
        curr_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        curr_hist = cv2.normalize(curr_hist, curr_hist, 0, 1, cv2.NORM_MINMAX)

        # Compara o histograma atual com o anterior
        diff = compare_histograms(prev_hist, curr_hist)

        # Verifica se a diferença ultrapassa o limiar
        if diff > threshold:
            # Ativa o alarme (faça o que for necessário)
            print("Movimento detectado!")

        # Atualiza o histograma anterior com o histograma atual
        prev_hist = curr_hist

        # Mostra o frame (opcional)
        cv2.imshow("Frame", frame)

        # Verifica se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
