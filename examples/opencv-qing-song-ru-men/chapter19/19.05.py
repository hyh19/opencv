# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/Vv4nMM

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255
center = (round(size / 2), round(size / 2))
axes = (100, 200)
for _ in range(0, 10):
    angle = np.random.randint(0, 361)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    thickness = np.random.randint(1, 9)
    cv2.ellipse(img, center, axes, angle, 0, 360, color, thickness)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
