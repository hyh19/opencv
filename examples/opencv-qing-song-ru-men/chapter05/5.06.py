# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3ZxNEBX

img = cv.imread("lena.bmp")
height, width = img.shape[:2]
M = cv.getRotationMatrix2D((width / 2, height / 2), 45, 0.6)
rotate = cv.warpAffine(img, M, (width, height))
cv.imshow("original", img)
cv.imshow("rotation", rotate)
cv.waitKey()
cv.destroyAllWindows()
