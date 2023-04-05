# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/ksyIBh

img = cv.imread('cc.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, 0, (0, 0, 255), 2)
x, y, w, h = cv.boundingRect(contours[0])
rect = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
cv.drawContours(img, [rect], -1, (255, 0, 0), 2)

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
