import cv2 as cv

img = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("before", img)

for row in range(10, 100):
    for col in range(80, 100):
        img[row, col] = 255
cv.imshow("after", img)

cv.waitKey()
cv.destroyAllWindows()
