# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('cc.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

red = (0, 0, 255)
blue = (255, 0, 0)

cv.drawContours(img, contours, 0, red, 2)
ellipse = cv.fitEllipse(contours[0])
print(f'ellipse = {ellipse}')
cv.ellipse(img, ellipse, blue, 3)

cv.imshow('result', img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/ik9Bjf