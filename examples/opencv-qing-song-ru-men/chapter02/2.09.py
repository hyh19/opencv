# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
# 测试读取、修改单个像素值
print("读取像素点img.item(3,2)=", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后像素点img.item(3,2)=", img.item(3, 2))
# 测试修改一个区域的像素值
cv.imshow("before", img)
for i in range(10, 100):
    for j in range(80, 100):
        img.itemset((i, j), 255)
cv.imshow("after", img)
cv.waitKey()
cv.destroyAllWindows()
