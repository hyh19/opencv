# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# --------读取并显示原始图像-----------------
o = cv.imread('ct.png')
cv.imshow("original", o)

# --------获取轮廓-----------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
cnt = contours[2]

# --------使用掩膜获取感兴趣区域的均值-----------------
mask = np.zeros(gray.shape, np.uint8)  # 构造mean所使用的掩膜，必须是单通道的
cv.drawContours(mask, [cnt], 0, (255, 255, 255), -1)
meanVal = cv.mean(o, mask=mask)  # mask是区域，所以必须是单通道的
print("meanVal=\n", meanVal)

# --------使用掩膜获取感兴趣区域并显示-----------------
masko = np.zeros(o.shape, np.uint8)
cv.drawContours(masko, [cnt], -1, (255, 255, 255), -1)
loc = cv.bitwise_and(o, masko)
cv.imshow("loc", loc)

# --------释放窗口-----------------
cv.waitKey()
cv.destroyAllWindows()
