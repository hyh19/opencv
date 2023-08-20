# -*- coding: utf-8 -*-
import cv2 as cv

bgr_img = cv.imread('lesson2.jpg')
hsv_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv_img, (5, 25, 0), (170, 166, 255))
roi_img = cv.bitwise_and(bgr_img, bgr_img, mask=mask)

cv.imshow('bgr', bgr_img)
cv.imshow('roi', roi_img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/GBWvl2
