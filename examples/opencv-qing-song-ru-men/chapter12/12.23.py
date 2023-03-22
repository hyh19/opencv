# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('hand.bmp')
cv.imshow("original", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

# --------------凸包----------------------
image1 = o.copy()
hull = cv.convexHull(contours[0])
cv.polylines(image1, [hull], True, (0, 255, 0), 2)
print("使用函数cv2.convexHull()构造的多边形是否是凸包：",
      cv.isContourConvex(hull))
cv.imshow("result1", image1)

# ------------逼近多边形--------------------
image2 = o.copy()
epsilon = 0.01 * cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
image2 = cv.drawContours(image2, [approx], 0, (0, 0, 255), 2)
print("使用函数cv2.approxPolyDP()构造的多边形是否是凸包：",
      cv.isContourConvex(approx))
cv.imshow("result2", image2)

# ------------释放窗口--------------------
cv.waitKey()
cv.destroyAllWindows()
