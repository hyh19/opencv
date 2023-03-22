# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('scharr.bmp', cv2.IMREAD_GRAYSCALE)
scharrxy11 = cv2.Scharr(o, cv2.CV_64F, 1, 1)
cv2.imshow("original", o)
cv2.imshow("xy11", scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()
