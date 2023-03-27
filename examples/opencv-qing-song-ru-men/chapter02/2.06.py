# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3lGMg13

img = cv.imread('lenacolor.png')
cv.imshow('before', img)
print('读取img[0,0]=', img[0, 0])
print('读取img[0,0,0]=', img[0, 0, 0])
print('读取img[0,0,1]=', img[0, 0, 1])
print('读取img[0,0,2]=', img[0, 0, 2])
print('读取img[50,0]=', img[50, 0])
print('读取img[100,0]=', img[100, 0])

# 区域1
for row in range(0, 50):
    for col in range(0, 100):
        for ch in range(0, 3):
            img[row, col, ch] = 255  # 白色

# 区域2
for row in range(50, 100):
    for col in range(0, 100):
        img[row, col] = [128, 128, 128]  # 灰色

# 区域3
for row in range(100, 150):
    for col in range(0, 100):
        img[row, col] = 0  # 黑色

cv.imshow('after', img)
print('修改后img[0,0]=', img[0, 0])
print('修改后img[0,0,0]=', img[0, 0, 0])
print('修改后img[0,0,1]=', img[0, 0, 1])
print('修改后img[0,0,2]=', img[0, 0, 2])
print('修改后img[50,0]=', img[50, 0])
print('修改后img[100,0]=', img[100, 0])

cv.waitKey()
cv.destroyAllWindows()

'''
读取img[0,0]= [125 137 226]
读取img[0,0,0]= 125
读取img[0,0,1]= 137
读取img[0,0,2]= 226
读取img[50,0]= [114 136 230]
读取img[100,0]= [ 75  55 155]
修改后img[0,0]= [255 255 255]
修改后img[0,0,0]= 255
修改后img[0,0,1]= 255
修改后img[0,0,2]= 255
修改后img[50,0]= [128 128 128]
修改后img[100,0]= [0 0 0]
'''
