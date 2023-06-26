import cv2

def equalize_histogram(frame):
    # Convertendo a imagem para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Equalizando o histograma
    equalized = cv2.equalizeHist(gray)
    
    # Convertendo a imagem de volta para BGR (colorida)
    equalized = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
    
    return equalized

def main():
    # Inicializando a captura de vídeo
    cap = cv2.VideoCapture(0)
    
    while True:
        # Lendo o próximo frame
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Equalizando o histograma do frame atual
        equalized_frame = equalize_histogram(frame)
        
        # Exibindo o frame original e o equalizado
        cv2.imshow("Original", frame)
        cv2.imshow("Equalized", equalized_frame)
        
        # Verificando se o usuário pressionou a tecla 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberando os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
