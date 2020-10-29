import cv2
import numpy as np


def make_gaussian_filter(img, n):
    mask = [[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]]
    img = np.pad(img, pad_width=1, mode='constant', constant_values=0)  # 0 패딩
    new_img = np.zeros((column, row), dtype=np.uint8)
    s = 0.0
    for i in range(1, column + 1):
        for j in range(1, row + 1):
            for x in range(n):
                for z in range(n):
                    s += mask[x][z] * img[i + x - 1][j + z - 1]
            new_img[i - 1][j - 1] = s
            s = 0.0
    return new_img


img = cv2.imread("../image/test_img21.png", cv2.IMREAD_GRAYSCALE)
column = len(img)
row = len(img[0])
cv2.imshow("Before",img)
cv2.imshow("After", make_gaussian_filter(img,3))
cv2.waitKey(0)
cv2.destroyAllWindows()