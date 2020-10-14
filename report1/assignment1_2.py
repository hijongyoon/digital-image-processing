import cv2


def kamma(img, value):
    for i in img:
        for j in range(len(i)):
           i[j] = ((i[j]/255) ** (1/value)) * 255  # 감마구하는 공식
    return img


img = cv2.imread("../image/test_img4.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("Before",img)
cv2.imshow("After", kamma(img,2.5))
cv2.waitKey(0)
cv2.destroyAllWindows()
