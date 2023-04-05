# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/wVD8zw

img = cv.imread('contours.bmp')
cv.imshow("img", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 0, 255), 5)
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

'''
>>> print(hierarchy)
[[[ 1 -1 -1 -1]
  [ 2  0 -1 -1]
  [-1  1 -1 -1]]]

>>> type(contours)
<class 'tuple'>

>>> type(contours[0])
<class 'numpy.ndarray'>

>>> print(contours[0].shape)
(4, 1, 2)
'''
