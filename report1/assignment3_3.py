import cv2
import numpy as np


def turn_to_binary(img):  # 이진화
    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j] = 255 if img[i][j] > 127 else 0
    return img


img1 = cv2.imread("../image/test_img15.png", cv2.IMREAD_GRAYSCALE)
img1 = turn_to_binary(img1)
img2 = cv2.imread("../image/test_img16.png", cv2.IMREAD_GRAYSCALE)
img2 = turn_to_binary(img2)
cv2.imshow("AND", img1 & img2)
cv2.imshow("OR", img1 | img2)
cv2.imshow("XOR", img1 ^ img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
