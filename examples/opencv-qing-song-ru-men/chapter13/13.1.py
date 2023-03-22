# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

o = cv2.imread("image/boat.jpg")
cv2.imshow("original", o)
plt.hist(o.ravel(), 256)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

# https://matplotlib.org/3.7.1/api/_as_gen/matplotlib.pyplot.hist.html
