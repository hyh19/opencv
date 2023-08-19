import cv2 as cv
import numpy as np

# 读文件
img = cv.imread('../images/hello.jpeg')

print(img.shape)

# 转变成单通道
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

r = cv.minAreaRect(contours[1])
box = cv.boxPoints(r)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 2)

x, y, w, h = cv.boundingRect(contours[1])
cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# minAreaRect: https://t.ly/MhzA
# boxPoints: https://t.ly/T0ij
# boundingRect: https://t.ly/ozJs
