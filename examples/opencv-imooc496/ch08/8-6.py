import cv2 as cv

img = cv.imread('../images/papper.png')

# 中值滤波
result = cv.medianBlur(img, ksize=5)

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# medianBlur: https://t.ly/mI_R
