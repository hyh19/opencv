# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/KURtUP

img1 = cv.imread('cs1.bmp')
img2 = cv.imread('cs2.bmp')
img3 = cv.imread('cc.bmp')

gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)

match11 = cv.matchShapes(gray1, gray1, 1, 0.0)
match12 = cv.matchShapes(gray1, gray2, 1, 0.0)
match13 = cv.matchShapes(gray1, gray3, 1, 0.0)

print(f'相同图像的 matchShapes = {match11}')
print(f'相似图像的 matchShapes = {match12}')
print(f'不相似图像的 matchShapes = {match13}')

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img3", img3)
cv.waitKey()
cv.destroyAllWindows()

'''
相同图像的 matchShapes = 0.0
相似图像的 matchShapes = 0.0001154058519395873
不相似图像的 matchShapes = 0.012935752303635306
'''
