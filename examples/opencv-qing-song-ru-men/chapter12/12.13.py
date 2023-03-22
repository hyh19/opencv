# -*- coding: utf-8 -*-
import cv2 as cv

# ---------------读取并显示原始图像------------------
o = cv.imread('cc.bmp')
cv.imshow("original", o)

# ---------------提取图像轮廓------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

# ---------------构造矩形边界------------------
x, y, w, h = cv.boundingRect(contours[0])
cv.rectangle(o, (x, y), (x + w, y + h), (0, 0, 255), 2)

# ---------------显示矩形边界------------------
cv.imshow("result", o)

cv.waitKey()
cv.destroyAllWindows()
