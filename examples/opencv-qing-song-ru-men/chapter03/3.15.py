# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3kPPX4b

# 读取原始载体图像
lena = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
# 读取水印图像
watermark = cv.imread("watermark.bmp", cv.IMREAD_GRAYSCALE)
# 将水印内的255处理为1，以方便嵌入
w = watermark[:, :] > 0
watermark[w] = 1
# 读取原始载体图像的shape值
r, c = lena.shape

# ============嵌入过程============
# 生成内部值都是254的数组
t254 = np.ones((r, c), dtype=np.uint8) * 254
# 获取lena图像的高7位
lenaH7 = cv.bitwise_and(lena, t254)
# 将watermark嵌入到lenaH7内
e = cv.bitwise_or(lenaH7, watermark)

# ============提取过程============
# 生成内部值都是1的数组
t1 = np.ones((r, c), dtype=np.uint8)
# 从载体图像内，提取水印图像
wm = cv.bitwise_and(e, t1)
print(wm)
# 将水印内的1处理为255以方便显示
w = wm[:, :] > 0
wm[w] = 255

# ============显示============
cv.imshow("lena", lena)
cv.imshow("watermark", watermark * 255)  # 当前watermark内最大值为1
cv.imshow("e", e)
cv.imshow("wm", wm)

cv.waitKey()
cv.destroyAllWindows()
