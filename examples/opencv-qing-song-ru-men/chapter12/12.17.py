# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('cc.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
rows, cols = image.shape[:2]
[vx, vy, x, y] = cv.fitLine(contours[0], cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv.line(o, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
