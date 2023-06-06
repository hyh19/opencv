# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 300
img = np.ones((size, size, 3), np.uint8) * 255
cv.rectangle(img, (50, 50), (size - 100, size - 50), (0, 0, 255), -1)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/zsFe3G
