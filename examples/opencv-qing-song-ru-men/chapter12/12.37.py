# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('ct.png')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
cnt = contours[2]  # coutours[0]、coutours[1]是左侧字母R

# --------使用掩膜获取感兴趣区域的最值-----------------
# 需要注意minMaxLoc处理的对象为灰度图像，本例中处理对象为灰度图像gray
# 如果希望获取彩色图像的，需要提取各个通道，将每个通道独立计算最值
mask = np.zeros(gray.shape, np.uint8)
mask = cv.drawContours(mask, [cnt], -1, 255, -1)
cv.imshow("mask", mask)
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(gray, mask=mask)
print("minVal=", minVal)
print("maxVal=", maxVal)
print("minLoc=", minLoc)
print("maxLoc=", maxLoc)

# --------使用掩膜获取感兴趣区域并显示-----------------
masko = np.zeros(o.shape, np.uint8)
masko = cv.drawContours(masko, [cnt], -1, (255, 255, 255), -1)
loc = cv.bitwise_and(o, masko)
cv.imshow("loc", loc)
# 显示灰度结果
loc_gray = cv.bitwise_and(gray, mask)
cv.imshow("loc_gray", loc_gray)

# --------释放窗口-----------------
cv.waitKey()
cv.destroyAllWindows()
