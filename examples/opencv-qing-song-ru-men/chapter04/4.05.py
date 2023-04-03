# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/HwXMyr

bgr = cv.imread("lenacolor.png")
rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
bgr1 = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow("bgr", bgr)
cv.imshow("rgb", rgb)
cv.imshow("bgr1", bgr1)
cv.waitKey()
cv.destroyAllWindows()
