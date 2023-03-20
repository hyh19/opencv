# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('sobel4.bmp', cv2.IMREAD_GRAYSCALE)
sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("original", o)
cv2.imshow("y", sobely)
cv2.waitKey()
cv2.destroyAllWindows()
