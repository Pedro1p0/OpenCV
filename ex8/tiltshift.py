import cv2
import numpy as np

def on_trackbar_height(val):
    global height
    height = val / 100

def on_trackbar_decay(val):
    global decay
    decay = val / 100

def on_trackbar_position(val):
    global position
    position = val / 100

def tilt_shift(image):
    height = int(image.shape[0] * 0.4)
    decay = 0.6
    position = 0.5

    cv2.namedWindow("tiltshift")
    cv2.createTrackbar("Height", "tiltshift", height, 100, on_trackbar_height)
    cv2.createTrackbar("Decay", "tiltshift", int(decay * 100), 100, on_trackbar_decay)
    cv2.createTrackbar("Position", "tiltshift", int(position * 100), 100, on_trackbar_position)
    
    while True:
        h, w = image.shape[:2]

        blurred = cv2.GaussianBlur(image, (0, 0), 2)
        mask = np.zeros((h, w), dtype=np.float32)
        mask[int((1 - height) * h):int(h * position), :] = 1
        mask = cv2.GaussianBlur(mask, (0, 0), 10)
        mask = cv2.normalize(mask, None, 0, 1, cv2.NORM_MINMAX)

        result = np.copy(image)
        for c in range(image.shape[2]):
            result[:, :, c] = image[:, :, c] * (1 - mask) + blurred[:, :, c] * (mask * decay)
        cv2.namedWindow("tiltshift", cv2.WINDOW_NORMAL)
        cv2.namedWindow("tiltshift")


        cv2.imshow("tiltshift", result)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

    cv2.destroyAllWindows()
    return result

if __name__ == "__main__":
    image = cv2.imread("/home/bolsistaspop/pedro-vitor/opencv/ex8/dom_pedro.jpg")
    result = tilt_shift(image)
    cv2.imwrite("output.jpg", result)
   
