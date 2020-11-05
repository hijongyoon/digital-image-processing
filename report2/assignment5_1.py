import cv2
import copy


def make_rgb():
    red_img, green_img, blue_img = copy.copy(image), copy.copy(image), copy.copy(image)    # r,g,b 이미지 만듬
    # opencv 에서는 b g r순
    blue_img[:, :, 1] = 0  # b g r 순이므로 b 값 빼고는 다 0
    blue_img[:, :, 2] = 0
    green_img[:, :, 0] = 0  # g 값 빼고는 다 0
    green_img[:, :, 2] = 0
    red_img[:, :, 0] = 0  # r 값 빼고는 다 0
    red_img[:, :, 1] = 0

    return red_img, green_img, blue_img


def make_cmy():
    cyan_img = green_img+blue_img    # cyan = b + g
    magenta_img = red_img+blue_img    # magenta = r + b
    yellow_img = red_img+green_img    # yellow = r + g

    return cyan_img, magenta_img, yellow_img


image = cv2.imread("../image/test_img5.jpeg", cv2.IMREAD_COLOR)
h, w = image.shape[:2]
cv2.imshow("original", image)  # 변환전 이미지 show
red_img, green_img, blue_img = make_rgb()
cyan_img, magenta_img, yellow_img = make_cmy()
cv2.imshow("red", red_img)
cv2.imshow("blue", blue_img)
cv2.imshow("green", green_img)
cv2.imshow("cyan", cyan_img)
cv2.imshow("magenta", magenta_img)
cv2.imshow("yellow", yellow_img)
cv2.waitKey(0)
cv2.destroyAllWindows()