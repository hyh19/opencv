import cv2 as cv
import numpy as np

# img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
# thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# print(f'img = \n{img}')
# print(f'thresh = {thresh}')
# print(f'res = \n{res}')

img = cv.imread('lena.bmp')
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
