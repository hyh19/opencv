# -*- coding: utf-8 -*-
import cv2 as cv

# ----------------计算图像1的Hu矩-------------------
o1 = cv.imread('cs1.bmp')
gray1 = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
HuM1 = cv.HuMoments(cv.moments(gray1)).flatten()

# ----------------计算图像2的Hu矩-------------------
o2 = cv.imread('cs3.bmp')
gray2 = cv.cvtColor(o2, cv.COLOR_BGR2GRAY)
HuM2 = cv.HuMoments(cv.moments(gray2)).flatten()

# ----------------计算图像3的Hu矩-------------------
o3 = cv.imread('lena.bmp')
gray3 = cv.cvtColor(o3, cv.COLOR_BGR2GRAY)
HuM3 = cv.HuMoments(cv.moments(gray3)).flatten()

# ---------打印图像1、图像2、图像3的特征值------------
print("o1.shape=", o1.shape)
print("o2.shape=", o2.shape)
print("o3.shape=", o3.shape)
print("cv.moments(gray1)=\n", cv.moments(gray1))
print("cv.moments(gray2)=\n", cv.moments(gray2))
print("cv.moments(gray3)=\n", cv.moments(gray3))
print("\nHuM1=\n", HuM1)
print("\nHuM2=\n", HuM2)
print("\nHuM3=\n", HuM3)

# ---------计算图像1与图像2、图像3的Hu矩之差----------------
print("\nHuM1-HuM2=", HuM1 - HuM2)
print("\nHuM1-HuM3=", HuM1 - HuM3)

# ---------显示图像----------------
cv.imshow("original1", o1)
cv.imshow("original2", o2)
cv.imshow("original3", o3)

cv.waitKey()
cv.destroyAllWindows()
