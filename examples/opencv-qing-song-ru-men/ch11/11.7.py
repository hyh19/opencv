# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread("lena.bmp")

# =================生成高斯金字塔======================
G0 = o
G1 = cv.pyrDown(G0)
G2 = cv.pyrDown(G1)
G3 = cv.pyrDown(G2)

# ===============生成拉普拉斯金字塔====================
L0 = G0 - cv.pyrUp(G1)  # 拉普拉斯金字塔第0层
L1 = G1 - cv.pyrUp(G2)  # 拉普拉斯金字塔第1层
L2 = G2 - cv.pyrUp(G3)  # 拉普拉斯金字塔第2层

# =================复原G0======================
RG0 = L0 + cv.pyrUp(G1)  # 通过拉普拉斯图像复原的原始图像G0
print("G0.shape=", G0.shape)
print("RG0.shape=", RG0.shape)
result = RG0 - G0  # 将RG0和G0做减法
# 计算result的绝对值，避免求和时负负为正3+(-3)=0
result = abs(result)
# 计算result所有元素的和
print("原始图像G0与恢复图像RG0差值的绝对值和：", np.sum(result))

# =================复原G1======================
RG1 = L1 + cv.pyrUp(G2)  # 通过拉普拉斯图像复原G1
print("G1.shape=", G1.shape)
print("RG1.shape=", RG1.shape)
result = RG1 - G1  # 将o和ro做减法
print("原始图像G1与恢复图像RG1差值的绝对值和：", np.sum(abs(result)))

# =================复原G2======================
RG2 = L2 + cv.pyrUp(G3)  # 通过拉普拉斯图像复原G2
print("G2.shape=", G2.shape)
print("RG2.shape=", RG2.shape)
result = RG2 - G2  # 将o和ro做减法
print("原始图像G2与恢复图像RG2差值的绝对值和：", np.sum(abs(result)))
