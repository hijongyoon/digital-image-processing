import cv2


def make_fre_histogram(img): # 빈도횟수를 저장한 histogram 만들기
    histogram = {}
    for i in range(256):
        histogram[i] = 0
    for i in img:
        for j in range(len(i)):
            histogram[i[j]] += 1
    return histogram


def make_accu_histogram(fre_histogram): # 누적 합을 가진 histogram 만들기
    for i in fre_histogram:
        if i == 0:
            continue
        fre_histogram[i] += fre_histogram[i-1]
    return fre_histogram


def normalization(img, acc_histogram, frequency): # 공식을 사용하여 정규화 하기
    for i in img:
        for j in range(len(i)):
            i[j] = acc_histogram[i[j]] * (1/frequency) * 255  # (누적 합 * 최대 명도)/영상 크기
    return img


img = cv2.imread("../image/test_img9.png", cv2.IMREAD_GRAYSCALE)
frequency = len(img[0]) * len(img)
acc_histogram = make_accu_histogram(make_fre_histogram(img))
cv2.imshow("Before",img)
cv2.imshow("After", normalization(img,acc_histogram,frequency))
cv2.waitKey(0)
cv2.destroyAllWindows()
