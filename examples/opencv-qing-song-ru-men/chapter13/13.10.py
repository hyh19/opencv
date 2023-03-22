# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("image/girl.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("image", image)

mask = np.zeros(image.shape, np.uint8)
mask[200:400, 200:400] = 255
cv.imshow("mask", mask)

image_mask = cv.bitwise_and(image, mask)
cv.imshow("image_mask", image_mask)

hist_image = cv.calcHist([image], [0], None, [256], [0, 255])
hist_mask = cv.calcHist([image], [0], mask, [256], [0, 255])
plt.plot(hist_image)
plt.plot(hist_mask)
plt.show()

cv.waitKey()
cv.destroyAllWindows()
