# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# --------------读取及显示原始图像--------------------
o = cv.imread('contours0.bmp')
cv.imshow("original", o)

# --------------获取轮廓--------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

# --------------计算各个轮廓的长度和、平均长度--------------------
n = len(contours)  # 获取轮廓个数
cntLen = []  # 存储各个轮廓的长度
for i in range(n):
    cntLen.append(cv.arcLength(contours[i], True))
    print("第" + str(i) + "个轮廓的长度:%d" % cntLen[i])
cntLenSum = np.sum(cntLen)  # 各个轮廓长度和
cntLenAvr = cntLenSum / n  # 各个轮廓长度平均值
print("各个轮廓的总长度为：%d" % cntLenSum)
print("各个轮廓的平均长度为：%d" % cntLenAvr)

# --------------显示超过平均值的轮廓--------------------
contoursImg = []
for i in range(n):
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv.drawContours(contoursImg[i],
                                      contours, i, (255, 255, 255), 3)
    if cv.arcLength(contours[i], True) > cntLenAvr:
        cv.imshow("contours[" + str(i) + "]", contoursImg[i])

cv.waitKey()
cv.destroyAllWindows()
