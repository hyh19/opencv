# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/sVLerU

img = cv.imread('hand.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, 0)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 轮廓
yellow = (0, 255, 255)
# 凸包
green = (0, 255, 0)
# 凸缺陷起点和终点
red = (0, 0, 255)
# 凸缺陷最远点
blue = (255, 0, 0)

cnt = contours[0]
cv.drawContours(img, contours, 0, yellow, 2)

hull = cv.convexHull(cnt, returnPoints=False)
defects = cv.convexityDefects(cnt, hull)
print(f'defects = \n{defects}')

for d in defects:
    start_index, end_index, far_index, dist = d[0]
    start_point = tuple(cnt[start_index][0])
    end_point = tuple(cnt[end_index][0])
    far_point = tuple(cnt[far_index][0])
    cv.line(img, start_point, end_point, green, 2)
    cv.circle(img, far_point, 3, blue, -1)

for h in hull:
    index = h[0]
    cv.circle(img, tuple(cnt[index][0]), 3, red, -1)

cv.imshow('result', img)
cv.waitKey()
cv.destroyAllWindows()

'''
defects = 
[[[    0   102    51 21878]]

 [[  103   184   150 13876]]

 [[  185   233   220  4168]]

 [[  233   238   235   256]]

 [[  238   240   239   247]]

 [[  240   294   255  2715]]

 [[  294   302   295   281]]

 [[  302   304   303   217]]

 [[  305   311   306   114]]

 [[  311   385   342 13666]]

 [[  385   389   386   395]]

 [[  389   489   435 20327]]]
'''
