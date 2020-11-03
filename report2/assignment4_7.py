import cv2
import numpy as np


def check(num):
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    return num


def make_LPF(having_noise, n):
    having_noise = np.pad(having_noise, pad_width=1, mode='constant', constant_values=0)  # 0 패딩
    removed_noise = np.zeros((column, row), dtype=np.uint8)
    s = 0.0
    for i in range(1, column + 1):
        for j in range(1, row + 1):
            for x in range(n):
                for z in range(n):
                    s += mask[x][z] * having_noise[i + x - 1][j + z - 1]
            removed_noise[i-1][j-1] = check(s)
            s = 0.0
    return removed_noise


def make_noise(img, std):  # 노이즈 생성
    having_noise = np.zeros(img.shape, dtype=np.float64)

    for i in range(column):
        for j in range(row):
            random_noise = std * np.random.normal()  # 노이지의 크기 * 표본편차로 가우시안 노이즈 생성
            val = img[i][j] + random_noise
            having_noise[i][j] = check(val)
    return having_noise


img = cv2.imread("../image/test_img5.jpg", cv2.IMREAD_GRAYSCALE)
mask = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
column = len(img)
row = len(img[0])
having_noise = np.uint8(make_noise(img, 32))
cv2.imshow("Before", having_noise)
cv2.imshow("After", make_LPF(having_noise, 3))
cv2.waitKey(0)
cv2.destroyAllWindows()