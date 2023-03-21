# -*- coding: utf-8 -*-
import cv2

# ----------------原始图像-------------------------
o = cv2.imread('cs.bmp')
cv2.imshow("original", o)

# ----------------获取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(binary,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)

# ----------------内部点A的距离-------------------------
ptA = (300, 150)
distA = cv2.pointPolygonTest(hull, ptA, True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'A', ptA, font, 1, (0, 255, 0), 3)
cv2.circle(image, ptA, 3, [255, 0, 0], -1)
print("distA=", distA)

# ----------------外部点B的距离-------------------------
ptB = (300, 250)
distB = cv2.pointPolygonTest(hull, ptB, True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'B', ptB, font, 1, (0, 255, 0), 3)
cv2.circle(image, ptB, 3, [255, 0, 0], -1)
print("distB=", distB)

# ------------正好处于边缘上的点C的距离-----------------
ptC = (423, 112)
distC = cv2.pointPolygonTest(hull, ptC, True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'C', ptC, font, 1, (0, 255, 0), 3)
cv2.circle(image, ptC, 3, [255, 0, 0], -1)
print("distC=", distC)
# print(hull)   #测试边缘到底在哪里，然后再使用确定位置的

# ----------------显示-------------------------
cv2.imshow("result", image)
cv2.waitKey()
cv2.destroyAllWindows()
