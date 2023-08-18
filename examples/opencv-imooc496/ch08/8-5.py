import cv2 as cv

img = cv.imread('../images/gaussian.png')

# 高斯滤波
result = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=1)

cv.imshow('result', result)
cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# GaussianBlur: https://t.ly/pQMK
