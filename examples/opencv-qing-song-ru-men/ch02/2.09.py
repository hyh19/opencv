# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)

# 读取、修改单个像素值
print(f'读取像素点 img.item(3,2) = {img_gray.item(3, 2)}')
img_gray.itemset((3, 2), 255)
print(f'修改后像素点 img.item(3,2) = {img_gray.item(3, 2)}')

# 修改一个区域的像素值
cv.imshow('before', img_gray)
for row in range(10, 100):
    for col in range(80, 100):
        img_gray.itemset((row, col), 255)
cv.imshow('after', img_gray)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3lE7UDd

'''
读取像素点 img.item(3,2) = 159
修改后像素点 img.item(3,2) = 255
'''
