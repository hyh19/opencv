# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("image/lenaNoise.png")
r = cv.blur(o, (5, 5))
cv.imshow("original", o)
cv.imshow("result", r)
cv.waitKey()
cv.destroyAllWindows()
