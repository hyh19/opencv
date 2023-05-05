# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lenacolor.png')

cv.imshow('before', img)
print(f'读取 img.item(0,0,0) = {img.item(0, 0, 0)}')
print(f'读取 img.item(0,0,1) = {img.item(0, 0, 1)}')
print(f'读取 img.item(0,0,2) = {img.item(0, 0, 2)}')

for row in range(0, 50):
    for col in range(0, 100):
        for ch in range(0, 3):
            img.itemset((row, col, ch), 255)

cv.imshow('after', img)
print(f'修改后 img.item(0,0,0) = {img.item(0, 0, 0)}')
print(f'修改后 img.item(0,0,1) = {img.item(0, 0, 1)}')
print(f'修改后 img.item(0,0,2) = {img.item(0, 0, 2)}')

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/I6T8zQ

'''
读取 img.item(0,0,0) = 125
读取 img.item(0,0,1) = 137
读取 img.item(0,0,2) = 226
修改后 img.item(0,0,0) = 255
修改后 img.item(0,0,1) = 255
修改后 img.item(0,0,2) = 255
'''
