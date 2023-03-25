# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/I6T8zQ

img = cv.imread("lenacolor.png")

cv.imshow("before", img)
print("读取img.item(0,0,0)=", img.item(0, 0, 0))
print("读取img.item(0,0,1)=", img.item(0, 0, 1))
print("读取img.item(0,0,2)=", img.item(0, 0, 2))

for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img.itemset((i, j, k), 255)  # 白色

cv.imshow("after", img)
print("修改后img.item(0,0,0)=", img.item(0, 0, 0))
print("修改后img.item(0,0,1)=", img.item(0, 0, 1))
print("修改后img.item(0,0,2)=", img.item(0, 0, 2))

cv.waitKey()
cv.destroyAllWindows()

"""
读取img.item(0,0,0)= 125
读取img.item(0,0,1)= 137
读取img.item(0,0,2)= 226
修改后img.item(0,0,0)= 255
修改后img.item(0,0,1)= 255
修改后img.item(0,0,2)= 255
"""
