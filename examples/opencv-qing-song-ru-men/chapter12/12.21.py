# -*- coding: utf-8 -*-
import cv2 as cv

# --------------读取并绘制原始图像------------------
o = cv.imread('hand.bmp')
cv.imshow("original", o)

# --------------提取轮廓------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

# --------------寻找凸包，得到凸包的角点------------------
hull = cv.convexHull(contours[0])

# --------------绘制凸包------------------
cv.polylines(o, [hull], True, (0, 255, 0), 2)

# --------------显示凸包------------------
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
