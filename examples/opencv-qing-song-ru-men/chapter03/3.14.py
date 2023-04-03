# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/meSEIZ

gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
key = np.random.randint(0, 256, size=gray.shape, dtype=np.uint8)

encryption = cv.bitwise_xor(gray, key)
decryption = cv.bitwise_xor(encryption, key)

cv.imshow('gray', gray)
cv.imshow('key', key)
cv.imshow('encryption', encryption)
cv.imshow('decryption', decryption)
cv.waitKey()
cv.destroyAllWindows()
