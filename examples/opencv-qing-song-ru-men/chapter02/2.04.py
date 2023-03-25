# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3JMl6hm

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:, 0:100, 0] = 255
img[:, 100:200, 1] = 255
img[:, 200:300, 2] = 255
print("img=\n", img)
cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
