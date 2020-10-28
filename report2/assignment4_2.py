import cv2
import numpy as np



def make_blurring(img):
    img = np.pad(img, pad_width=1, mode='constant', constant_values=0) # 0 패딩
    new_img = np.zeros((column, row), dtype=np.uint8)
    for i in range(1, column+1):
        for j in range(1, row+1):
            new_img[i - 1][j - 1] = (int(img[i - 1][j - 1]) + int(img[i - 1][j]) + int(img[i - 1][j + 1]) + int(img[i][j - 1]) +int(img[i][j]) + int(img[i][j + 1]) + int(img[i + 1][j - 1]) + int(img[i + 1][j]) + int(img[i + 1][j + 1])) * (1 / 9)
    return new_img

img = cv2.imread("../image/test_img5.jpg", cv2.IMREAD_GRAYSCALE)
column = len(img)
row = len(img[0])
cv2.imshow("After", make_blurring(img))
cv2.waitKey(0)
cv2.destroyAllWindows()