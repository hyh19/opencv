import cv2

img = cv2.imread('lena.png')

# 双边滤波
dst = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow('dst', dst)
cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# bilateralFilter: https://t.ly/F0FP
