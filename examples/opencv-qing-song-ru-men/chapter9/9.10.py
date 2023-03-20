# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('scharr.bmp', cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(o, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv2.imshow("original", o)
cv2.imshow("xy", scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()
