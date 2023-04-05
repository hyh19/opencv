# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/DLY55L

img = cv.imread('cs.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 凸包
green = (0, 255, 0)
# 点
red = (0, 0, 255)
# 文字
blue = (255, 0, 0)

hull = cv.convexHull(contours[0])
cv.polylines(img, [hull], True, green, 2)

ptA = (300, 150)
distA = cv.pointPolygonTest(hull, ptA, True)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'A', ptA, font, 1, blue, 2)
cv.circle(img, ptA, 5, red, -1)
print(f'distA = {distA}')

ptB = (300, 250)
distB = cv.pointPolygonTest(hull, ptB, True)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'B', ptB, font, 1, blue, 2)
cv.circle(img, ptB, 5, red, -1)
print(f'distB = {distB}')

ptC = (423, 112)
distC = cv.pointPolygonTest(hull, ptC, True)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'C', ptC, font, 1, blue, 2)
cv.circle(img, ptC, 5, red, -1)
print(f'distC = {distC}')

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

'''
distA = 16.891650862259112
distB = -81.17585848021565
distC = -0.0
'''
