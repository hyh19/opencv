# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255
font = cv.FONT_HERSHEY_SIMPLEX
red = (0, 0, 255)
green = (0, 255, 0)
cv.putText(img, 'OpenCV', (0, 150), font, 3, red, 15)
cv.putText(img, 'OpenCV', (0, 250), font, 3, green, 15, cv.FONT_HERSHEY_SCRIPT_SIMPLEX, True)
cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/8kl2Ry
