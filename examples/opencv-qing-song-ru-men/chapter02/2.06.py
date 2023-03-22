# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("lenacolor.png")
cv.imshow("before", img)
print("访问img[0,0]=", img[0, 0])
print("访问img[0,0,0]=", img[0, 0, 0])
print("访问img[0,0,1]=", img[0, 0, 1])
print("访问img[0,0,2]=", img[0, 0, 2])
print("访问img[50,0]=", img[50, 0])
print("访问img[100,0]=", img[100, 0])

# 区域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img[i, j, k] = 255  # 白色

# 区域2
for i in range(50, 100):
    for j in range(0, 100):
        img[i, j] = [128, 128, 128]  # 灰色

# 区域3
for i in range(100, 150):
    for j in range(0, 100):
        img[i, j] = 0  # 黑色

cv.imshow("after", img)

print("修改后img[0,0]=", img[0, 0])
print("修改后img[0,0,0]=", img[0, 0, 0])
print("修改后img[0,0,1]=", img[0, 0, 1])
print("修改后img[0,0,2]=", img[0, 0, 2])
print("修改后img[50,0]=", img[50, 0])
print("修改后img[100,0]=", img[100, 0])

cv.waitKey()
cv.destroyAllWindows()
