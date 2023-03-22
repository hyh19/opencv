# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('cc.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cntArea = cv.contourArea(contours[0])
equiDiameter = np.sqrt(4 * cntArea / np.pi)
print(equiDiameter)
cv.circle(o, (100, 100), int(equiDiameter / 2), (0, 0, 255), 3)  # 展示等直径大小的圆
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
