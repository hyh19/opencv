# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(o, cv.CV_64F, 1, 0, ksize=3)
sobely = cv.Sobel(o, cv.CV_64F, 0, 1, ksize=3)
sobelx = cv.convertScaleAbs(sobelx)  # 转回uint8
sobely = cv.convertScaleAbs(sobely)
sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

scharrx = cv.Scharr(o, cv.CV_64F, 1, 0)
scharry = cv.Scharr(o, cv.CV_64F, 0, 1)
scharrx = cv.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

cv.imshow("original", o)
cv.imshow("sobelxy", sobelxy)
cv.imshow("scharrxy", scharrxy)
cv.waitKey()
cv.destroyAllWindows()
