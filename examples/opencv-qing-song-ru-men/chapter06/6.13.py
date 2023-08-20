# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('tiffany.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_thresh = cv.threshold(img_gray, thresh=127, maxval=255, type=cv.THRESH_BINARY)
thresh, img_otsu = cv.threshold(img_gray, thresh=0, maxval=255, type=cv.THRESH_OTSU)

cv.imshow('img', img)
cv.imshow('gray', img_gray)
cv.imshow('thresh', img_thresh)
cv.imshow('otus', img_otsu)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/hgFGdG
