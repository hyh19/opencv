# -*- coding: utf-8 -*-
import cv2 as cv

# ----------------原图--------------------------
img = cv.imread('hand.bmp')
cv.imshow('original', img)

# ----------------查找轮廓--------------------------
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, 0)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_TREE,
                                              cv.CHAIN_APPROX_SIMPLE)

# ----------------获取轮廓的凸包和凸缺陷--------------------------
cnt = contours[0]
hull = cv.convexHull(cnt, returnPoints=False)
defects = cv.convexityDefects(cnt, hull)
print("defects=\n", defects)

# ----------------显示轮廓--------------------------
cv.drawContours(img, contours, 0, (0, 255, 0), 2)

# ----------------显示凸缺陷--------------------------
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img, start, end, [0, 0, 255], 2)
    cv.circle(img, far, 3, [255, 0, 0], -1)

# ----------------显示凸包点集--------------------------
for i in range(hull.shape[0]):
    index = hull[i][0]
    cv.circle(img, tuple(cnt[index][0]), 3, [255, 0, 255], -1)

# ----------------显示结果、释放图像--------------------------
cv.imshow('result', img)
cv.waitKey(0)
cv.destroyAllWindows()
