# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/ycuVnN

lena = cv.imread('lena512.bmp', cv.IMREAD_UNCHANGED)
dollar = cv.imread('dollar.bmp', cv.IMREAD_UNCHANGED)
cv.imshow('lena', lena)
cv.imshow('dollar', dollar)

# Extract face regions
lena_face = lena[220:400, 250:350]
dollar_face = dollar[160:340, 200:300]

# Blend the faces
blended_face = cv.addWeighted(lena_face, 0.6, dollar_face, 0.4, 0)

# Replace the dollar face with the blended face
dollar[160:340, 200:300] = blended_face

# Show the result
cv.imshow('result', dollar)
cv.waitKey()
cv.destroyAllWindows()
