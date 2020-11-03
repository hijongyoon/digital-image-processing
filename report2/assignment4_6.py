import cv2
import numpy as np


def check(num):
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    return num


def make_LPF(img, n):
    img = np.pad(img, pad_width=1, mode='constant', constant_values=0)  # 0 패딩
    unsharp_img = np.zeros((column, row), dtype=np.uint8)
    high_boost_img = np.zeros((column, row), dtype=np.uint8)
    s = 0.0
    for i in range(1, column + 1):
        for j in range(1, row + 1):
            for x in range(n):
                for z in range(n):
                    s += mask[x][z] * img[i + x - 1][j + z - 1]
            unsharp_img[i - 1][j - 1] = check(img[i - 1][j - 1] - check(s))
            high_boost_img[i - 1][j - 1] = check(1.7 * img[i - 1][j - 1] - check(s))
            s = 0.0
    return unsharp_img, high_boost_img


img = cv2.imread("../image/test_img21.png", cv2.IMREAD_GRAYSCALE)
mask = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
column = len(img)
row = len(img[0])
cv2.imshow("Before", img)
unsharp_img, high_boost_img = make_LPF(img, 3)
cv2.imshow("unsharp", unsharp_img)
cv2.imshow("high-boost", high_boost_img)
cv2.waitKey(0)
cv2.destroyAllWindows()