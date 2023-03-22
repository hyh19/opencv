# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread("image/boatGray.bmp")
cv.imshow("original", o)

hist = cv.calcHist([o], [0], None, [256], [0, 255])
plt.plot(hist, color='b')
plt.show()

cv.waitKey()
cv.destroyAllWindows()
