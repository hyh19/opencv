# -*- coding: utf-8 -*-
import cv2
import numpy as np

o = cv2.imread("erode.bmp", cv2.IMREAD_UNCHANGED)
kernel = np.ones((9, 9), np.uint8)
erosion = cv2.erode(o, kernel, iterations=5)
cv2.imshow("original", o)
cv2.imshow("erosion", erosion)
cv2.waitKey()
cv2.destroyAllWindows()
