import numpy as np
import cv2

img = np.zeros((480, 640, 3), np.uint8)

# 从矩阵中读取某个元素的值
# print(img[100, 80])

# count = 0
# while count < 200:
#     img[count, 80, 0] = 255
#     count += 1


# 对矩阵中某个元素赋值
count = 0
while count < 200:
    # BGR
    img[count, 100] = [255, 255, 255]
    count += 1

cv2.imshow('img', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
