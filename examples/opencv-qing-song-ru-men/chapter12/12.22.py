# -*- coding: utf-8 -*-
import cv2

# ----------------原图--------------------------
img = cv2.imread('hand.bmp')
cv2.imshow('original', img)

# ----------------查找轮廓--------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(binary,
                                              cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)

# ----------------获取轮廓的凸包和凸缺陷--------------------------
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print("defects=\n", defects)

# ----------------显示轮廓--------------------------
cv2.drawContours(img, contours, 0, (0, 255, 0), 2)

# ----------------显示凸缺陷--------------------------
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 0, 255], 2)
    cv2.circle(img, far, 3, [255, 0, 0], -1)

# ----------------显示凸包点集--------------------------
for i in range(hull.shape[0]):
    index = hull[i][0]
    cv2.circle(img, tuple(cnt[index][0]), 3, [255, 0, 255], -1)

# ----------------显示结果、释放图像--------------------------
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
