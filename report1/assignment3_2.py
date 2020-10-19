import cv2
import numpy as np


def find_avg(noise_set):  # 평균
    img = np.zeros(noise_set[0].shape, dtype=np.float64)
    result = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            for x in range(len(noise_set)):
                result += noise_set[x][i][j]
            img[i][j] = result // len(noise_set)
            result = 0
    return img


def make_noise(img, std):  # 노이즈 생성
    having_noise = np.zeros(img.shape, dtype=np.float64)

    for i in range(len(img)):
        for j in range(len(img[0])):
            random_noise = std * np.random.normal()  # 노이지의 크기 * 표본편차로 가우시안 노이즈 생성
            val = img[i][j] + random_noise
            if val > 255:
                having_noise[i][j] = 255
            elif val < 0:
                having_noise[i][j] = 0
            else:
                having_noise[i][j] = val
    return having_noise


img = cv2.imread("../image/test_img4.jpg", cv2.IMREAD_GRAYSCALE)
noise_set = [make_noise(img,32) for _ in range(8)]  # 노이즈를 첨가한 이미지 8개 생성
noise_set2 = [make_noise(img,32) for _ in range(2)]  # 노이즈를 첨가한 이미지 2개 생성
cv2.imshow("8", np.uint8(find_avg(noise_set)))  # 그걸 평균 내는 것
cv2.imshow("2", np.uint8(find_avg(noise_set2)))
cv2.waitKey(0)
cv2.destroyAllWindows()