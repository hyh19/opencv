# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('tiffany.bmp')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh1, thresh_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
thresh2, otsu_img = cv.threshold(gray_img, 0, 255, cv.THRESH_OTSU)

cv.imshow('img', img)
cv.imshow('gray', gray_img)
cv.imshow('thresh', thresh_img)
cv.imshow('otus', otsu_img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/hgFGdG
