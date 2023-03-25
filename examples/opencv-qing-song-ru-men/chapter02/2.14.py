# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/ovNKcR

img = cv.imread("lenacolor.png", cv.IMREAD_UNCHANGED)
cv.imshow("img", img)
mosaic = np.random.randint(0, 256, (180, 100, 3))
img[220:400, 250:350] = mosaic
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
