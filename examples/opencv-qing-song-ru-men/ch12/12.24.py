# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('cs.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 凸包
green = (0, 255, 0)
# 顶点
red = (0, 0, 255)
# 文字
blue = (255, 0, 0)

hull = cv.convexHull(contours[0])
cv.polylines(img, [hull], True, green, 2)

for point, point_name in zip([(300, 150), (300, 250), (423, 112)], ['A', 'B', 'C']):
    dist = cv.pointPolygonTest(hull, point, True)
    cv.putText(img, point_name, point, cv.FONT_HERSHEY_SIMPLEX, 1, blue, 2)
    cv.circle(img, point, 5, red, -1)
    print(f'dist{point_name} = {dist}')

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/DLY55L

'''
distA = 16.891650862259112
distB = -81.17585848021565
distC = -0.0
'''
