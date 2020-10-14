import cv2


def reverse(img):
    for i in img:
        for j in range(len(i)):
           i[j] = 255 - i[j]  # 255를 뺌으로서 반전 영상 만들기
    return img


img = cv2.imread("../image/test_img4.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("Before",img)
cv2.imshow("After", reverse(img))
cv2.waitKey(0)
cv2.destroyAllWindows()