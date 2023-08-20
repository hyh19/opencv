# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('hand.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

green = (0, 255, 0)
red = (0, 0, 255)

img_hull = img.copy()
hull = cv.convexHull(cnt)
print(f'cv.isContourConvex(hull) = {cv.isContourConvex(hull)}')
cv.polylines(img_hull, [hull], True, green, 2)
cv.imshow("convexHull", img_hull)

img_poly = img.copy()
epsilon = 0.01 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
print(f'cv.isContourConvex(approx) = {cv.isContourConvex(approx)}')
cv.drawContours(img_poly, [approx], 0, (0, 0, 255), 2)
cv.imshow("approxPolyDP", img_poly)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/V9NwBW
