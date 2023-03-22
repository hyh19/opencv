# -*- coding: utf-8 -*-
import cv2 as cv

# -----------原始图像o1边缘--------------------
o1 = cv.imread('cs.bmp')
cv.imshow("original1", o1)
gray1 = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
ret, binary1 = cv.threshold(gray1, 127, 255, cv.THRESH_BINARY)
image, contours1, hierarchy = cv.findContours(binary1,
                                               cv.RETR_LIST,
                                               cv.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]

# -----------原始图像o2边缘--------------------
o2 = cv.imread('cs3.bmp')
cv.imshow("original2", o2)
gray2 = cv.cvtColor(o2, cv.COLOR_BGR2GRAY)
ret, binary2 = cv.threshold(gray2, 127, 255, cv.THRESH_BINARY)
image, contours2, hierarchy = cv.findContours(binary2,
                                               cv.RETR_LIST,
                                               cv.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]

# -----------原始图像o3边缘--------------------
o3 = cv.imread('hand.bmp')
cv.imshow("original3", o3)
gray3 = cv.cvtColor(o3, cv.COLOR_BGR2GRAY)
ret, binary3 = cv.threshold(gray3, 127, 255, cv.THRESH_BINARY)
image, contours3, hierarchy = cv.findContours(binary3,
                                               cv.RETR_LIST,
                                               cv.CHAIN_APPROX_SIMPLE)
cnt3 = contours3[0]

# -----------构造距离提取算子--------------------
sd = cv.createShapeContextDistanceExtractor()

# -----------计算距离--------------------
d1 = sd.computeDistance(cnt1, cnt1)
print("自身距离d1=", d1)
d2 = sd.computeDistance(cnt1, cnt2)
print("旋转缩放后距离d2=", d2)
d3 = sd.computeDistance(cnt1, cnt3)
print("不相似对象距离d3=", d3)

# -----------显示距离--------------------
cv.waitKey()
cv.destroyAllWindows()
