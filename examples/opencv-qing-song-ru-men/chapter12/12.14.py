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

rect = cv.minAreaRect(contours[0])
print("返回值rect:\n", rect)

points = cv.boxPoints(rect)
print("\n转换后的points：\n", points)

points = np.int0(points)  # 取整
cv.drawContours(o, [points], 0, (0, 0, 255), 2)
cv.imshow("result", o)

cv.waitKey()
cv.destroyAllWindows()
