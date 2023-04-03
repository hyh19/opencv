# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/y8Jstr

bgr = cv.imread("barbara.bmp")
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
hue, sat, val = cv.split(hsv)
val[:, :] = 255
hsv = cv.merge([hue, sat, val])
art = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("bgr", bgr)
cv.imshow("art", art)
cv.waitKey()
cv.destroyAllWindows()
