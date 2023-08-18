import cv2 as cv

img = cv.imread('../images/dog.jpeg')

# 均值滤波
result = cv.blur(img, ksize=(5, 5))

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# blur: https://t.ly/xzjZ
