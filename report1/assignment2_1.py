import cv2


def transition(img, low, high):
    for i in img:
        for j in range(len(i)):
            result = ((i[j] - low) / (high - low)) * 255  # 기본 명암 대비 스트레칭 수행 공식
            if result < 0:
                i[j] *= (result * -1)
            elif result > 255:
                i[j] = 255
    return img


def find_low_high(img):  # 가장 큰 값과 가장 작은 값 찾기
    low = img[0][0]
    high = img[0][1]
    for i in img:
        for j in range(len(i)):
            if low > i[j]:
                low = i[j]
            if high < i[j]:
                high = i[j]
    return low, high


img = cv2.imread("../image/test_img5.jpeg", cv2.IMREAD_GRAYSCALE)
low, high = find_low_high(img)

cv2.imshow("Before",img)
cv2.imshow("After", transition(img, low, high))
cv2.waitKey(0)
cv2.destroyAllWindows()
