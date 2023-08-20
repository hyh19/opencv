# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread("image/boat.jpg")
cv.imshow("original", o)
plt.hist(o.ravel(), 256)
plt.show()
cv.waitKey()
cv.destroyAllWindows()

# https://matplotlib.org/3.7.1/api/_as_gen/matplotlib.pyplot.hist.html
