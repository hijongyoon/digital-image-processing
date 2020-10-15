import cv2
import numpy as np

def highlight(img,start,end):
    for i in img:
        for j in range(len(i)):
            if (np.all(i[j] >= start)) and np.all(i[j] <= end) :  # 값이 128 부터 192 까지는 전부 255로 만들기
                i[j] = 255
    return img


img = cv2.imread("../image/test_img4.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("Before",img)
cv2.imshow("After", highlight(img,128.0,192.0))
cv2.waitKey(0)
cv2.destroyAllWindows()
