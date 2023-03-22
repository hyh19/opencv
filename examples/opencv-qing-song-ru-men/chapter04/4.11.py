# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/41YrMRU

img = cv.imread("barbara.bmp")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
v[:, :] = 255
newHSV = cv.merge([h, s, v])
art = cv.cvtColor(newHSV, cv.COLOR_HSV2BGR)
cv.imshow("img", img)
cv.imshow("art", art)
cv.waitKey()
cv.destroyAllWindows()
