import numpy as np
import cv2

img = np.zeros((480, 640, 3), np.uint8)

# 从矩阵中读取某个元素的值
print(img[100, 80])

example = 2
if example == 0:
    count = 0
    while count < 200:
        img[count, 80] = 255
        count += 1
elif example == 1:
    count = 0
    while count < 200:
        img[count, 80, 0] = 255
        count += 1
elif example == 2:
    count = 0
    while count < 200:
        img[count, 100] = [255, 255, 0]
        count += 1

cv2.imshow('img', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
