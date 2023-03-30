# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/w71f0O

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255

for _ in range(0, 100):
    centerX = np.random.randint(0, high=size)
    centerY = np.random.randint(0, high=size)
    radius = np.random.randint(5, high=size / 5)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    cv2.circle(img, (centerX, centerY), radius, color, -1)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
