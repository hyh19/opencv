# -*- coding: utf-8 -*-
import cv2

lena = cv2.imread("lenacolor.png")
rgb = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
cv2.imshow("lena", lena)
cv2.imshow("rgb", rgb)
cv2.imshow("bgr", bgr)
cv2.waitKey()
cv2.destroyAllWindows()
