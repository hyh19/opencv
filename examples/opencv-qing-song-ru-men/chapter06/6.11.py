# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("computer.jpg", 0)
t1, thd = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
athdMEAN = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 5)
athdGAUS = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 5)
cv.imshow("img", img)
cv.imshow("thd", thd)
cv.imshow("athdMEAN", athdMEAN)
cv.imshow("athdGAUS", athdGAUS)
cv.waitKey()
cv.destroyAllWindows()
