# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('cc.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
area, trgl = cv.minEnclosingTriangle(contours[0])
print("area=", area)
print("trgl:", trgl)
for i in range(0, 3):
    cv.line(o, tuple(trgl[i][0].astype(int)),
             tuple(trgl[(i + 1) % 3][0].astype(int)), (0, 0, 255), 2)
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()

# numpy.ndarray.astype: https://bit.ly/3Tyhmof
