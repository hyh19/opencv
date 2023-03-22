# -*- coding: utf-8 -*-
import cv2 as cv

# --------------读取3幅原始图像--------------------
o1 = cv.imread('cs1.bmp')
o2 = cv.imread('cs2.bmp')
o3 = cv.imread('cc.bmp')

# ----------打印3幅原始图像的shape属性值-------------
print("o1.shape=", o1.shape)
print("o2.shape=", o2.shape)
print("o3.shape=", o3.shape)

# --------------色彩空间转换--------------------
gray1 = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(o2, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(o3, cv.COLOR_BGR2GRAY)

# -------------进行Hu矩匹配--------------------
ret0 = cv.matchShapes(gray1, gray1, 1, 0.0)
ret1 = cv.matchShapes(gray1, gray2, 1, 0.0)
ret2 = cv.matchShapes(gray1, gray3, 1, 0.0)

# --------------打印差值--------------------
print("相同图像的matchShape=", ret0)
print("相似图像的matchShape=", ret1)
print("不相似图像的matchShape=", ret2)

# --------------显示3幅原始图像--------------------
cv.imshow("original1", o1)
cv.imshow("original2", o2)
cv.imshow("original3", o3)

cv.waitKey()
cv.destroyAllWindows()
