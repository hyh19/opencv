import cv2 as cv

img_gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
cv.imshow('before', img_gray)

for row in range(10, 100):
    for col in range(80, 100):
        img_gray[row, col] = 255
cv.imshow('after', img_gray)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/7J3nnq
