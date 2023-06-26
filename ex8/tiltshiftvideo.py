import cv2
import numpy as np

def on_trackbar_blend(val):
    global alfa
    alfa = val / alfa_slider_max
    cv2.addWeighted(image1, 1-alfa, imageTop, alfa, 0.0, blended)
    cv2.imshow("addweighted", blended)

def on_trackbar_line(val):
    image1.copyTo(imageTop)
    limit = val * 255 / top_slider_max
    if limit > 0:
        tmp = image2[0:limit, 0:256]
        tmp.copyTo(imageTop[0:limit, 0:256])
    on_trackbar_blend(alfa_slider)

def tilt_shift_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    alfa_slider = 0
    alfa_slider_max = 100
    top_slider = 0
    top_slider_max = 100

    ret, frame = cap.read()
    if not ret:
        print("Erro ao ler o quadro inicial.")
        cap.release()
        return
    
    image1 = frame
    image2 = cv2.imread("blend2.jpg")
    imageTop = np.copy(image1)
    blended = np.copy(image1)

    cv2.namedWindow("addweighted", cv2.WINDOW_NORMAL)
    cv2.namedWindow("tiltshift", cv2.WINDOW_NORMAL)

    cv2.createTrackbar("Alpha x {}".format(alfa_slider_max), "addweighted", alfa_slider, alfa_slider_max, on_trackbar_blend)
    on_trackbar_blend(alfa_slider)

    cv2.createTrackbar("Scanline x {}".format(top_slider_max), "addweighted", top_slider, top_slider_max, on_trackbar_line)
    on_trackbar_line(top_slider)

    writer = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        blurred = cv2.GaussianBlur(frame, (0, 0), 2)
        mask = np.zeros((h, w), dtype=np.float32)
        mask[int((1 - alfa) * h):int(h * position), :] = 1
        mask = cv2.GaussianBlur(mask, (0, 0), 10)
        mask = cv2.normalize(mask, None, 0, 1, cv2.NORM_MINMAX)

        result = np.copy(frame)
        for c in range(frame.shape[2]):
            result[:, :, c] = frame[:, :, c] * (1 - mask) + blurred[:, :, c] * (mask * decay)

        cv2.imshow("tiltshift", result)

        if writer is None:
            writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 25, (w, h))
        writer.write(result)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

    if writer is not None:
        writer.release()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "input_video.mp4"
    output_path = "output_video.mp4"
    tilt_shift_video(video_path, output_path)
