import cv2

img = cv2.imread('gaussian.png')

# 高斯滤波
dst = cv2.GaussianBlur(img, (5, 5), sigmaX=1)

cv2.imshow('dst', dst)
cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# GaussianBlur: https://t.ly/pQMK
