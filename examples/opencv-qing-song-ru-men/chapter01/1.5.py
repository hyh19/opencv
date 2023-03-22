# -*- coding: utf-8 -*-
import cv2

lena = cv2.imread("lenacolor.png")
cv2.imshow("demo", lena)
cv2.waitKey()
cv2.destroyWindow("demo")
