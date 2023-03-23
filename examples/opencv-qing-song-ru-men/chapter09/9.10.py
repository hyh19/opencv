# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharrx = cv.Scharr(o, cv.CV_64F, 1, 0)
scharry = cv.Scharr(o, cv.CV_64F, 0, 1)
scharrx = cv.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv.imshow('original', o)
cv.imshow('xy', scharrxy)
cv.waitKey()
cv.destroyAllWindows()
