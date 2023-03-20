# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('scharr.bmp', cv2.IMREAD_GRAYSCALE)
scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)
cv2.imshow("original", o)
cv2.imshow("y", scharry)
cv2.waitKey()
cv2.destroyAllWindows()
