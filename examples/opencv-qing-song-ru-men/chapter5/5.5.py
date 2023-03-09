# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://bit.ly/3T3oh8z

img = cv2.imread("lena.bmp")
height, width = img.shape[:2]
x = 100
y = 200
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(img, M, (width, height))
cv2.imshow("original", img)
cv2.imshow("move", move)
cv2.waitKey()
cv2.destroyAllWindows()
