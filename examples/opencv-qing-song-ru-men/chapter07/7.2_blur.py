# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("image/lenaNoise.png")
r5 = cv.blur(o, (5, 5))
r30 = cv.blur(o, (30, 30))
cv.imshow("original", o)
cv.imshow("result5", r5)
cv.imshow("result30", r30)
cv.waitKey()
cv.destroyAllWindows()
