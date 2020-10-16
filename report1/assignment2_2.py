import cv2


def transition(img, low, high):
    for i in img:
        for j in range(len(i)):
            if low >= i[j]:  # old pixel <= low
                i[j] = 0
            elif high <= i[j]:  # low <= old pixel <= high
                i[j] = 255
            else:  # high <= old pixel
                i[j] = (i[j] - low) / (high - low) * 255
    return img



def find_low_high(img):
    low = img[0][0]
    high = img[0][1]
    for i in img:
        for j in range(len(i)):
            if low > i[j]:
                low = i[j]
            if high < i[j]:
                high = i[j]
    high -= 50
    low += 50
    return low, high


img = cv2.imread("../image/test_img4.jpeg", cv2.IMREAD_GRAYSCALE)
low, high = find_low_high(img)
cv2.imshow("Before",img)
cv2.imshow("After", transition(img, low, high))
cv2.waitKey(0)
cv2.destroyAllWindows()
