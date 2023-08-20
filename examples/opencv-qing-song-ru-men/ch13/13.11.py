# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

# -----------读取原始图像---------------
img = cv.imread('image/equ.bmp', cv.IMREAD_GRAYSCALE)

# -----------直方图均衡化处理---------------
equ = cv.equalizeHist(img)

# -----------显示均衡化前后的直方图---------------
cv.imshow("original", img)
cv.imshow("result", equ)

# -----------显示均衡化前后的直方图---------------
plt.figure("原始图像直方图")
plt.hist(img.ravel(), 256)
plt.figure("均衡化结果直方图")
plt.hist(equ.ravel(), 256)
plt.show()

# ----------等待释放窗口---------------------
cv.waitKey()
cv.destroyAllWindows()
