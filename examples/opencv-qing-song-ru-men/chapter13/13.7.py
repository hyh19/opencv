# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

o = cv2.imread("image/boatGray.bmp")
cv2.imshow("original", o)

hist = cv2.calcHist([o], [0], None, [256], [0, 255])
plt.plot(hist, color='b')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
