# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/HUfFTS

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255
(centerX, centerY) = (round(img.shape[1] / 2), round(img.shape[0] / 2))

for radius in range(5, round(size / 2), 12):
    cv2.circle(img, (centerX, centerY), radius, (0, 0, 255), 3)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
