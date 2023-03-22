# -*- coding: utf-8 -*-
import cv2 as cv

# -----------读取原始图像--------------------
o1 = cv.imread('cs.bmp')
o2 = cv.imread('cs3.bmp')
o3 = cv.imread('hand.bmp')
cv.imshow("original1", o1)
cv.imshow("original2", o2)
cv.imshow("original3", o3)

# -----------色彩转换--------------------
gray1 = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(o2, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(o3, cv.COLOR_BGR2GRAY)

# -----------阈值处理--------------------
ret, binary1 = cv.threshold(gray1, 127, 255, cv.THRESH_BINARY)
ret, binary2 = cv.threshold(gray2, 127, 255, cv.THRESH_BINARY)
ret, binary3 = cv.threshold(gray3, 127, 255, cv.THRESH_BINARY)

# -----------提取轮廓--------------------
image, contours1, hierarchy = cv.findContours(binary1,
                                               cv.RETR_LIST,
                                               cv.CHAIN_APPROX_SIMPLE)
image, contours2, hierarchy = cv.findContours(binary2,
                                               cv.RETR_LIST,
                                               cv.CHAIN_APPROX_SIMPLE)
image, contours3, hierarchy = cv.findContours(binary3,
                                               cv.RETR_LIST,
                                               cv.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]

# -----------构造距离提取算子--------------------
hd = cv.createHausdorffDistanceExtractor()

# -----------计算距离--------------------
d1 = hd.computeDistance(cnt1, cnt1)
print("自身Hausdorff距离d1=", d1)
d2 = hd.computeDistance(cnt1, cnt2)
print("旋转缩放后Hausdorff距离d2=", d2)
d3 = hd.computeDistance(cnt1, cnt3)
print("不相似对象Hausdorff距离d3=", d3)

# -----------显示距离--------------------
cv.waitKey()
cv.destroyAllWindows()
