# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3lE7UDd

img = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)

# 测试读取、修改单个像素值
print("读取像素点img.item(3,2)=", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后像素点img.item(3,2)=", img.item(3, 2))

# 测试修改一个区域的像素值
cv.imshow("before", img)
for row in range(10, 100):
    for col in range(80, 100):
        img.itemset((row, col), 255)
cv.imshow("after", img)

cv.waitKey()
cv.destroyAllWindows()

"""
读取像素点img.item(3,2)= 159
修改后像素点img.item(3,2)= 255
"""
