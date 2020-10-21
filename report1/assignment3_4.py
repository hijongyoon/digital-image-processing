import cv2
import numpy as np

img = cv2.imread("../image/test_img5.jpg", cv2.IMREAD_GRAYSCALE)

bit = [1, 2, 4, 8, 16, 32, 64, 128]  # 마지막 비트 부터 최상위 비트를 의미
bit_img = []

for x in range(len(bit)):
    image = np.zeros(img.shape, dtype=np.float64)
    for i in range(len(image)):
        for j in range(len(image[0])):
            value = img[i][j] & bit[x]
            image[i][j] = value
    bit_img.append(image)

for x in range(8):
    cv2.imshow(str(x+1),bit_img[x])
cv2.waitKey(0)
cv2.destroyAllWindows()