# -*- coding: utf-8 -*-
import cv2
import numpy as np

o = cv2.imread("lena.bmp")
G0 = o
G1 = cv2.pyrDown(G0)
L0 = o - cv2.pyrUp(G1)
RO = L0 + cv2.pyrUp(G1)  # 通过拉普拉斯图像复原的原始图像
print("O.shape=", o.shape)
print("RO.shape=", RO.shape)
result = RO - o  # 将o和ro做减法
# 计算result的绝对值，避免求和时负负为正3+(-3)=0
result = abs(result)
# 计算result所有元素的和
print("原始图像O与恢复图像RO差值的绝对值和：", np.sum(result))
