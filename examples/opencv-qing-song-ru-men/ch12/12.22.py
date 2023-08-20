# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('hand.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, 0)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 轮廓
yellow = (0, 255, 255)
# 凸缺陷起点和终点的连线
green = (0, 255, 0)
# 凸缺陷最远点
blue = (255, 0, 0)
# 凸包上的顶点
red = (0, 0, 255)

cnt = contours[0]
cv.drawContours(img, contours, 0, yellow, 2)

hull = cv.convexHull(cnt, returnPoints=False)
defects = cv.convexityDefects(cnt, hull)
print(f'defects = \n{defects}')

img_defects = img.copy()
for d in defects:
    start_index, end_index, far_index, dist = d[0]
    start_point = tuple(cnt[start_index][0])
    end_point = tuple(cnt[end_index][0])
    far_point = tuple(cnt[far_index][0])
    cv.line(img_defects, start_point, end_point, green, 2)
    cv.circle(img_defects, far_point, 3, blue, -1)
    cv.imshow('defects', img_defects)

img_hull = img.copy()
for h in hull:
    index = h[0]
    cv.circle(img_hull, tuple(cnt[index][0]), 3, red, -1)
    cv.imshow('hull', img_hull)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/sVLerU

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
