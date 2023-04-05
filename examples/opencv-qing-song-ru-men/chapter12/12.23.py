# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/V9NwBW

img = cv.imread('hand.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

green = (0, 255, 0)
red = (0, 0, 255)

img1 = img.copy()
hull = cv.convexHull(cnt)
print(f'cv.isContourConvex(hull) = {cv.isContourConvex(hull)}')
cv.polylines(img1, [hull], True, green, 2)
cv.imshow("convexHull", img1)

img2 = img.copy()
epsilon = 0.01 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
print(f'cv.isContourConvex(approx) = {cv.isContourConvex(approx)}')
cv.drawContours(img2, [approx], 0, (0, 0, 255), 2)
cv.imshow("approxPolyDP", img2)

cv.waitKey()
cv.destroyAllWindows()
