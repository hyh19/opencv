# -*- coding: utf-8 -*-
import cv2 as cv

# ----------------原始图像-------------------------
o = cv.imread('cs.bmp')
cv.imshow("original", o)

# ----------------获取凸包------------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
hull = cv.convexHull(contours[0])
image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
cv.polylines(image, [hull], True, (0, 255, 0), 2)

# ----------------内部点A的距离-------------------------
ptA = (300, 150)
distA = cv.pointPolygonTest(hull, ptA, True)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(image, 'A', ptA, font, 1, (0, 255, 0), 3)
cv.circle(image, ptA, 3, [255, 0, 0], -1)
print("distA=", distA)

# ----------------外部点B的距离-------------------------
ptB = (300, 250)
distB = cv.pointPolygonTest(hull, ptB, True)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(image, 'B', ptB, font, 1, (0, 255, 0), 3)
cv.circle(image, ptB, 3, [255, 0, 0], -1)
print("distB=", distB)

# ------------正好处于边缘上的点C的距离-----------------
ptC = (423, 112)
distC = cv.pointPolygonTest(hull, ptC, True)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(image, 'C', ptC, font, 1, (0, 255, 0), 3)
cv.circle(image, ptC, 3, [255, 0, 0], -1)
print("distC=", distC)
# print(hull)   #测试边缘到底在哪里，然后再使用确定位置的

# ----------------显示-------------------------
cv.imshow("result", image)
cv.waitKey()
cv.destroyAllWindows()
