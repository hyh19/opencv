import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/JKuhVr

img = cv.imread('water_coins.jpeg')
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

_, binary_inv = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow("binary_inv", binary_inv)

kernel = np.ones((3, 3), np.int8)
open1 = cv.morphologyEx(binary_inv, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow("open", open1)

dilate = cv.dilate(open1, kernel, iterations=1)
cv.imshow("dilate", dilate)

cv.waitKey()
cv.destroyAllWindows()
