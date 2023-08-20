# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255
centerX = centerY = round(size / 2)

for radius in range(5, round(size / 2), 12):
    cv.circle(img, (centerX, centerY), radius, (0, 0, 255), 3)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/HUfFTS
