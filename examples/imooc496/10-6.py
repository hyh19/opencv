import cv2
import numpy as np

# 读文件
img = cv2.imread('hello.jpeg')

print(img.shape)

# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

x, y, w, h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# minAreaRect: t.ly/MhzA
# boxPoints: t.ly/T0ij
# boundingRect: t.ly/ozJs
