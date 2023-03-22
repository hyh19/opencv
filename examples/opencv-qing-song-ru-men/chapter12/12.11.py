# -*- coding: utf-8 -*-
import cv2 as cv

# ---------------读取并显示原始图像------------------
o = cv.imread('cc.bmp')

# ---------------提取图像轮廓------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

# ---------------返回顶点及边长------------------
x, y, w, h = cv.boundingRect(contours[0])
print("顶点及长宽的点形式:")
print("x=", x)
print("y=", y)
print("w=", w)
print("h=", h)

# ---------------仅有一个返回值的情况------------------
rect = cv.boundingRect(contours[0])
print("\n顶点及长宽的元组（tuple）形式：")
print("rect=", rect)

o = cv.drawContours(o, contours, 0, (0, 0, 255), 5)
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
