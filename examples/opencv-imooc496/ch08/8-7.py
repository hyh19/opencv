import cv2 as cv

img = cv.imread('../images/lena.png')

# 双边滤波
result = cv.bilateralFilter(img, d=7, sigmaColor=20, sigmaSpace=50)

cv.imshow('result', result)
cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# bilateralFilter: https://t.ly/F0FP
