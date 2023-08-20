# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread("image/girl.bmp")
cv.imshow("original", o)

histb = cv.calcHist([o], [0], None, [256], [0, 255])
histg = cv.calcHist([o], [1], None, [256], [0, 255])
histr = cv.calcHist([o], [2], None, [256], [0, 255])
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.show()

cv.waitKey()
cv.destroyAllWindows()
