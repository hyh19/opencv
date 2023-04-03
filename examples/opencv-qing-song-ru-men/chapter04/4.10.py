# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/GBWvl2

bgr = cv.imread('lesson2.jpg')
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
hue, sat, val = cv.split(hsv)

hue_mask = cv.inRange(hue, 5, 170)
sat_mask = cv.inRange(sat, 25, 166)
mask = hue_mask & sat_mask
roi = cv.bitwise_and(bgr, bgr, mask=mask)

cv.imshow('bgr', bgr)
cv.imshow('roi', roi)
cv.waitKey()
cv.destroyAllWindows()
