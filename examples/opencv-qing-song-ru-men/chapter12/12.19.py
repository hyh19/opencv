# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3FDLBEv

# ----------------读取并显示原始图像-------------------------------
o = cv.imread('cc.bmp')
cv.imshow("original", o)

# ----------------获取轮廓-------------------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

# ----------------epsilon=0.1*周长-------------------------------
adp = o.copy()
epsilon = 0.1 * cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
adp = cv.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv.imshow("result0.1", adp)

# ----------------epsilon=0.09*周长-------------------------------
adp = o.copy()
epsilon = 0.09 * cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
adp = cv.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv.imshow("result0.09", adp)

# ----------------epsilon=0.055*周长-------------------------------
adp = o.copy()
epsilon = 0.055 * cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
adp = cv.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv.imshow("result0.055", adp)

# ----------------epsilon=0.05*周长-------------------------------
adp = o.copy()
epsilon = 0.05 * cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
adp = cv.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv.imshow("result0.05", adp)

# ----------------epsilon=0.02*周长-------------------------------
adp = o.copy()
epsilon = 0.02 * cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
adp = cv.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv.imshow("result0.02", adp)

# ----------------等待释放窗口-------------------------------
cv.waitKey()
cv.destroyAllWindows()
