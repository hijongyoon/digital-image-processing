import cv2
import numpy as np


def make_yCbCr(img):
    blue, green, red = img[0], img[1], img[2]
    y = 0.299 * red + 0.587 * green + 0.114 * blue
    Cr = 0.500 * red - 0.419 * green - 0.0813 * blue + 128
    Cb = -0.169 * red - 0.331 * green + 0.500 * blue + 128
    return np.array([y, Cr, Cb], dtype=np.float32)

img = cv2.imread("../image/test_img6.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("Before", img)
height = img.shape[0]
width = img.shape[1]

new_img = np.zeros(np.shape(img), dtype=np.float32)
for h in range(height):
    for w in range(width):
        new_img[h, w] = make_yCbCr(img[h, w])
img_y = np.uint8(np.clip(new_img[:,:,0], 0, 255))
img_Cr = np.uint8(np.clip(new_img[:,:,1], 0, 255))
img_Cb = np.uint8(np.clip(new_img[:,:,2], 0, 255))
cv2.imshow("y",img_y)
cv2.imshow("Cr", img_Cr)
cv2.imshow("Cb", img_Cb)
cv2.waitKey(0)
cv2.destroyAllWindows()