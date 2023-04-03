# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3kPPX4b
# 运行结果 https://is.gd/404PE9

# 读取原始载体图像
lena = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
# 读取水印图像
watermark_img = cv.imread('watermark.bmp', cv.IMREAD_GRAYSCALE)
# 将水印内的 255 处理为 1，以方便嵌入
watermark_img[watermark_img[:, :] > 0] = 1

# ========嵌入过程========
# 读取原始载体图像的 shape 值
rows, cols = lena.shape
# 生成内部值都是 254 的提取矩阵
m254 = np.ones((rows, cols), dtype=np.uint8) * 254
# 获取 lena 图像的高 7 位
lena_h7 = cv.bitwise_and(lena, m254)
# 将 watermark 嵌入到 lena_h7 内
embedded_img = cv.bitwise_or(lena_h7, watermark_img)

# ========提取过程========
# 生成内部值都是 1 的提取矩阵
m1 = np.ones((rows, cols), dtype=np.uint8)
# 从载体图像内，提取水印图像
extracted_img = cv.bitwise_and(embedded_img, m1)
# 将水印内的 1 处理为 255 以方便显示
extracted_img[extracted_img[:, :] > 0] = 255

cv.imshow('lena', lena)
# 当前 watermark_img 内最大值为 1
cv.imshow('watermark_img', watermark_img * 255)
cv.imshow('embedded_img', embedded_img)
cv.imshow('extracted_img', extracted_img)
cv.waitKey()
cv.destroyAllWindows()
