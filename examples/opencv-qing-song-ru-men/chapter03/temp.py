import cv2 as cv
import numpy as np

lena = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
watermark_img = cv.imread('watermark.bmp', cv.IMREAD_GRAYSCALE)
watermark_img[watermark_img > 0] = 1

m254 = np.ones(lena.shape, dtype=np.uint8) * 254
lena_h7 = cv.bitwise_and(lena, m254)
embedded_img = cv.bitwise_or(lena_h7, watermark_img)

m1 = np.ones(lena.shape, dtype=np.uint8)
extracted_img = cv.bitwise_and(embedded_img, m1)
extracted_img[extracted_img > 0] = 255

cv.imshow('lena', lena)
cv.imshow('watermark_img', watermark_img * 255)
cv.imshow('embedded_img', embedded_img)
cv.imshow('extracted_img', extracted_img)
cv.waitKey()
cv.destroyAllWindows()

