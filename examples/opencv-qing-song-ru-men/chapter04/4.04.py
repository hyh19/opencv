# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/Wro8lh

bgr = cv.imread("lenacolor.png")
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
bgr1 = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

cv.imshow("bgr", bgr)
cv.imshow("gray", gray)
cv.imshow("bgr1", bgr1)
cv.waitKey()
cv.destroyAllWindows()
