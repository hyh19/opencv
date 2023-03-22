# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

lena = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
r, c = lena.shape
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
encryption = cv.bitwise_xor(lena, key)
decryption = cv.bitwise_xor(encryption, key)
cv.imshow("lena", lena)
cv.imshow("key", key)
cv.imshow("encryption", encryption)
cv.imshow("decryption", decryption)
cv.waitKey()
cv.destroyAllWindows()
