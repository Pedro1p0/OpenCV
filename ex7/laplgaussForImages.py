import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=",")
        print("\n")

cap = cv2.imread('/home/bolsistaspop/pedro-vitor/opencv/ex7/dom_pedro.jpg', cv2.IMREAD_GRAYSCALE)
cap = cv2.flip(cap, 1)

cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)

media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111,
         0.1111, 0.1111, 0.1111, 0.1111]

mask = np.array([[0.1111, 0.1111, 0.1111],
                 [0.1111, 0.1111, 0.1111],
                 [0.1111, 0.1111, 0.1111]], dtype=np.float32)


absolut = 1  # calcs abs of the image

while True:
    
    framegray = cap
    if framegray is not None and framegray.size > 0:
        cv2.imshow("original", framegray)

    frame32f = framegray.astype(float)
    frameFiltered = cv2.filter2D(frame32f, -1, mask, borderType=cv2.BORDER_REPLICATE)
    
    if absolut:
        frameFiltered = cv2.convertScaleAbs(frameFiltered)


    result = frameFiltered.astype("uint8")

    cv2.imshow("filtroespacial", result)

    key = cv2.waitKey(10)
    if key == 27:
        break  # esc pressed!
    elif key == ord('a'):
        absolut = not absolut
    elif key == ord('m'):
        mask = cv2.Mat(3, 3, cv2.CV_32F, media)
        printmask(mask)
    elif key == ord('g'):
        # Define outro filtro aqui
        pass

cv2.destroyAllWindows()
