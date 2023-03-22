# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

o = cv2.imread("image/girl.bmp")
cv2.imshow("original", o)

histb = cv2.calcHist([o], [0], None, [256], [0, 255])
histg = cv2.calcHist([o], [1], None, [256], [0, 255])
histr = cv2.calcHist([o], [2], None, [256], [0, 255])
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
