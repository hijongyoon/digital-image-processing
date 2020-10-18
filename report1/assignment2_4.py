import cv2
import numpy as np


def make_fre_histogram(img):  # 빈도횟수를 저장한 histogram 만들기
    histogram = {}
    for i in range(256):
        histogram[i] = 0
    for i in img:
        for j in range(len(i)):
            histogram[i[j]] += 1
    return histogram


def make_accu_histogram(fre_histogram):  # 누적 합을 가진 histogram 만들기
    for i in fre_histogram:
        if i == 0:
            continue
        fre_histogram[i] += fre_histogram[i - 1]
    return fre_histogram


def normalization(img, acc_histogram, frequency):  # 공식을 사용하여 정규화 하기
    for i in img:
        for j in range(len(i)):
            i[j] = acc_histogram[i[j]] * (1 / frequency) * 255
    return img


def required_normalization(required_histogram, the_max, the_min):
    m_sum_of_schist = [0] * 256
    for i in range(256):
        m_sum_of_schist[i] = round((required_histogram[i] - the_min) * 255 / (the_max - the_min))
    return m_sum_of_schist


def make_specification():
    table = [0] * 256  # 룩업 테이블
    top = 255
    bottom = top - 1
    new_img = np.zeros(img1.shape, dtype=np.float64)
    while True:  # 룩업 테이블을 만듦(역평활화)
        for i in range(m_sum_of_schist[bottom], m_sum_of_schist[top] + 1):
            table[i] = top
        top = bottom
        bottom = bottom - 1
        if bottom < -1:
            break
    for i in range(len(normalization_img)):  # 룩업 테이블을 이용해 역변환
        for j in range(len(normalization_img[0])):
            x = normalization_img[i][j]
            new_img[i][j] = table[x]
    return np.uint8(new_img)


img1 = cv2.imread("../image/test_img21.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../image/test_img22.png", cv2.IMREAD_GRAYSCALE)
frequency = len(img1[0]) * len(img1)  # 총 픽셀 수
acc_histogram = make_accu_histogram(make_fre_histogram(img1))  # 원본 누적합 반환
normalization_img = normalization(img1, acc_histogram, frequency)  # 원본 평활화
required_histogram = make_accu_histogram(make_fre_histogram(img2))  # 원하는 이미지 누적합
the_min = min(required_histogram.values())  # 최소
the_max = max(required_histogram.values())  # 최대
m_sum_of_schist = required_normalization(required_histogram, the_max, the_min)  # 원하는 영상 평활화
cv2.imshow("Before", img1)
cv2.imshow("After", make_specification())  # 룩업 테이블을 이용한 명세화
cv2.waitKey(0)
