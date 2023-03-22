# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("lena.bmp")
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("img", img)
cv2.imshow("rst", rst)
cv2.waitKey()
cv2.destroyAllWindows()
