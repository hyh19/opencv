# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(256, 256, 3), dtype=np.uint8)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/40xbtty
