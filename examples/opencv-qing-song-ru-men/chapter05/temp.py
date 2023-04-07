import cv2 as cv
import numpy as np

img = cv.imread('test.bmp')
res = cv.resize(img, None, fx=2, fy=0.5)
print(f'img.shape = {img.shape}')
print(f'res.shape = {res.shape}')
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
