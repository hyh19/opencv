# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("computer.jpg", 0)
t1, thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
athdMEAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
athdGAUS = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
cv2.imshow("img", img)
cv2.imshow("thd", thd)
cv2.imshow("athdMEAN", athdMEAN)
cv2.imshow("athdGAUS", athdGAUS)
cv2.waitKey()
cv2.destroyAllWindows()
