# -*- coding: utf-8 -*-
import cv2

# ---------------读取并显示原始图像------------------
o = cv2.imread('cc.bmp')
cv2.imshow("original", o)

# ---------------提取图像轮廓------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(binary,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)

# ---------------构造矩形边界------------------
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(o, (x, y), (x + w, y + h), (0, 0, 255), 2)

# ---------------显示矩形边界------------------
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()
