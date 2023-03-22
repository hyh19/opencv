# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image/girl.bmp", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)

mask = np.zeros(image.shape, np.uint8)
mask[200:400, 200:400] = 255
cv2.imshow("mask", mask)

image_mask = cv2.bitwise_and(image, mask)
cv2.imshow("image_mask", image_mask)

hist_image = cv2.calcHist([image], [0], None, [256], [0, 255])
hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 255])
plt.plot(hist_image)
plt.plot(hist_mask)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
