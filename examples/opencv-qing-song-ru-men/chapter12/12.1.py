# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('contours.bmp')
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(binary,
                                              cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_SIMPLE)
o = cv2.drawContours(o, contours, -1, (0, 0, 255), 5)
cv2.imshow("result", o)
cv2.waitKey()
cv2.destroyAllWindows()
