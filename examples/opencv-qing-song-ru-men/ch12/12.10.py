# -*- coding: utf-8 -*-
import cv2 as cv

img1 = cv.imread('cs1.bmp')
img2 = cv.imread('cs2.bmp')
img3 = cv.imread('cc.bmp')

img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
img3_gray = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)

match11 = cv.matchShapes(img1_gray, img1_gray, 1, 0.0)
match12 = cv.matchShapes(img1_gray, img2_gray, 1, 0.0)
match13 = cv.matchShapes(img1_gray, img3_gray, 1, 0.0)

print(f'相同图像的 matchShapes = {match11}')
print(f'相似图像的 matchShapes = {match12}')
print(f'不相似图像的 matchShapes = {match13}')

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img3", img3)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/KURtUP

'''
相同图像的 matchShapes = 0.0
相似图像的 matchShapes = 0.0001154058519395873
不相似图像的 matchShapes = 0.012935752303635306
'''
