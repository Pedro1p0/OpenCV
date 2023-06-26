import cv2

def main():
    # Listando as câmeras disponíveis
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        else:
            print(f"Camera {index}: {cap.get(cv2.CAP_PROP_BACKEND_NAME)}")
        cap.release()
        index += 1

if __name__ == '__main__':
    main()
