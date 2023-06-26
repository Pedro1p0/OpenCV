import cv2
import numpy as np

def kmeans_with_random_centers(image, nClusters, nRodadas):
    samples = image.reshape((-1, 3)).astype(np.float32)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, centers = cv2.kmeans(samples, nClusters, None, criteria, nRodadas, flags)
    centers = np.uint8(centers)

    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)

    return segmented_image


nClusters = 8
nRodadas = 1
num_executions = 10

input_image_path = "ex12/cafe.jpeg"
output_prefix = "output_image"

input_image = cv2.imread(input_image_path)
if input_image is None:
    print("Error opening image:", input_image_path)
    exit()

for i in range(num_executions):
    segmented_image = kmeans_with_random_centers(input_image, nClusters, nRodadas)

    output_image_name = f"{output_prefix}_execution_{i+1}.jpg"
    cv2.imwrite(output_image_name, segmented_image)

print("Images saved successfully.")
