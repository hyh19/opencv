# -*- coding: utf-8 -*-
import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo1", lena)
cv2.imshow("demo2", lena)
cv2.waitKey()
cv2.destroyAllWindows()
