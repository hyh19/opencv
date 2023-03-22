# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('sobel4.bmp', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o, -1, 1, 0)
cv2.imshow("original", o)
cv2.imshow("x", sobelx)
cv2.waitKey()
cv2.destroyAllWindows()
