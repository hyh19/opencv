import cv2

img = cv2.imread('images/dog.jpeg')

# 均值滤波
dst = cv2.blur(img, (5, 5))

cv2.imshow('dst', dst)
cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# blur: https://t.ly/xzjZ
