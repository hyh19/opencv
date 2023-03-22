# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lena512.bmp", cv.IMREAD_UNCHANGED)
dollar = cv.imread("dollar.bmp", cv.IMREAD_UNCHANGED)
cv.imshow("lena", lena)
cv.imshow("dollar", dollar)
face = lena[220:400, 250:350]
dollar[160:340, 200:300] = face
cv.imshow("result", dollar)
cv.waitKey()
cv.destroyAllWindows()
