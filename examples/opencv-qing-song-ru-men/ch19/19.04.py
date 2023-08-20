# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255

for _ in range(0, 100):
    centerX = np.random.randint(0, high=size)
    centerY = np.random.randint(0, high=size)
    radius = np.random.randint(5, high=size / 5)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    cv.circle(img, (centerX, centerY), radius, color, -1)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/w71f0O
