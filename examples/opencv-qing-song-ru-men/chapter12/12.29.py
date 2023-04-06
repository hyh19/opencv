# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/sTe9N8

img = cv.imread('cc.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, (0, 0, 255), 2)
x, y, w, h = cv.boundingRect(contours[0])
cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
cnt_area = cv.contourArea(contours[0])
rect_area = w * h
print(f'extend = {cnt_area / rect_area}')
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
