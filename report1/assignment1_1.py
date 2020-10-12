import cv2
import numpy


def threshold(img, pivot):
    for i in img:
        for j in range(len(i)):
            if i[j] < pivot:  # pivot 으로 넘어온 값보다 작으면 0
                i[j] = 0
            else:
                i[j] = 255  # 크면 255
    return img


img = cv2.imread("../image/test_img4.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Before", img)
cv2.imshow("After", threshold(img, 127))
cv2.waitKey(0)
cv2.destroyAllWindows()
