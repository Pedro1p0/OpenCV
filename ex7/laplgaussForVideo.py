import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=", ")
        print()

def main():
    cap = cv2.VideoCapture(0)  # open the default camera
    media = np.array([[0.1111, 0.1111, 0.1111],
                     [0.1111, 0.1111, 0.1111],
                     [0.1111, 0.1111, 0.1111]])
    gauss = np.array([[0.0625, 0.125, 0.0625],
                      [0.125, 0.25, 0.125],
                      [0.0625, 0.125, 0.0625]])
    horizontal = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
    vertical = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])
    laplacian = np.array([[0, -1, 0],
                          [-1, 4, -1],
                          [0, -1, 0]])
    boost = np.array([[0, -1, 0],
                      [-1, 5.2, -1],
                      [0, -1, 0]])

    cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
    cv2.namedWindow("original", cv2.WINDOW_NORMAL)

    mask = np.float32(media)
    absolut = 1

    while True:
        ret, frame = cap.read()  # get a new frame from camera

        if not ret:
            print("Não foi possível ler o próximo frame")
            break

        framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        framegray = cv2.flip(framegray, 1)
        cv2.imshow("original", framegray)

        frame32f = np.float32(framegray)
        frameFiltered = cv2.filter2D(frame32f, -1, mask, borderType=cv2.BORDER_CONSTANT)

        if absolut:
            frameFiltered = cv2.absdiff(frameFiltered, 0)

        frameFiltered = np.uint8(frameFiltered)
        cv2.imshow("filtroespacial", frameFiltered)

        key = cv2.waitKey(10) & 0xFF
        if key == 27:
            break  # esc pressed!
        elif key == ord('a'):
            absolut = not absolut
        elif key == ord('m'):
            mask = np.float32(media)
            printmask(mask)
        elif key == ord('g'):
            mask = np.float32(gauss)
            printmask(mask)
        elif key == ord('h'):
            mask = np.float32(horizontal)
            printmask(mask)
        elif key == ord('v'):
            mask = np.float32(vertical)
            printmask(mask)
        elif key == ord('l'):
            mask = np.float32(laplacian)
            printmask(mask)
        elif key == ord('b'):
            mask = np.float32(boost)
            printmask(mask)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
