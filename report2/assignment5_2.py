import cv2
import numpy as np


def make_hsi(img):
    blue, green, red = img[0], img[1], img[2]
    intensity = np.mean(img)  # r, g, b의 평균 구함
    if red == blue == green:  # gray scale 일때
        hue = 0
        saturation = 0
    else:  # color 일때
        min_rgb = min(img)
        saturation = 1 - (min_rgb / intensity)
        s = ((red - green) + (red - blue)) / (2 * np.sqrt((red - green) ** 2 + (red - blue) * (green - blue)))
        hue = np.arccos(s) * 180 / np.pi  # radian 으로 변환
        if blue > green:
            hue = 360 - hue
        hue /= 360
    return np.array([hue, saturation, intensity], dtype=np.float32)


img1 = cv2.imread("../image/test_img29.png", cv2.IMREAD_COLOR)
cv2.imshow("Before", img1)
height = img1.shape[0]
width = img1.shape[1]

sub_img = img1 / 255  # 정규화 왜하는지 모름
img2 = np.zeros(np.shape(img1), dtype=np.float32)
for h in range(height):
    for w in range(width):
        img2[h, w] = make_hsi(sub_img[h, w])  # 픽셀마다 hsi 로 변경
img_h = np.uint8(np.clip(img2[:, :, 0] * 255, 0, 255))
img_s = np.uint8(np.clip(img2[:, :, 1] * 255, 0, 255))
img_i = np.uint8(np.clip(img2[:, :, 2] * 255, 0, 255))
cv2.imshow("Hue", img_h)
cv2.imshow("Saturation", img_s)
cv2.imshow("Intensity", img_i)
cv2.waitKey(0)
cv2.destroyAllWindows()