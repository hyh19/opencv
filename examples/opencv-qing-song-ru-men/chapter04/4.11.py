# -*- coding: utf-8 -*-
import cv2 as cv

bgr_img = cv.imread('barbara.bmp')
hsv_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)
hsv_img[:, :, 2] = 255
art = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
cv.imshow('bgr', bgr_img)
cv.imshow('art', art)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/y8Jstr
