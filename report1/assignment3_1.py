import cv2


def add_image(img1, img2):
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            result = int(img1[i][j]) + int(img2[i][j])
            img1[i][j] = 255 if result > 255 else result
    return img1


def min_image(img1,img2):
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            result = int(img1[i][j]) - int(img2[i][j])
            img1[i][j] = 0 if result < 0 else result
    return img1


img1 = cv2.imread("../image/test_img4.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../image/test_img14.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("add", add_image(img1,img2))
cv2.imshow("min", min_image(img1,img2))
cv2.waitKey(0)
cv2.destroyAllWindows()