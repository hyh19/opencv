# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lena512.bmp", cv.IMREAD_UNCHANGED)
dollar = cv.imread("dollar.bmp", cv.IMREAD_UNCHANGED)
cv.imshow("lena", lena)
cv.imshow("dollar", dollar)
face1 = lena[220:400, 250:350]
face2 = dollar[160:340, 200:300]
add = cv.addWeighted(face1, 0.6, face2, 0.4, 0)
dollar[160:340, 200:300] = add
cv.imshow("result", dollar)
cv.waitKey()
cv.destroyAllWindows()
