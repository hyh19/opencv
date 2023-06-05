import cv2 as cv
import numpy as np

img = cv.imread('water_coins.jpeg')
cv.imshow("img", img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", img_gray)

_, img_binary_inv = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow("binary_inv", img_binary_inv)

kernel = np.ones((3, 3), np.int8)
img_open = cv.morphologyEx(img_binary_inv, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow("open", img_open)

img_dilate = cv.dilate(img_open, kernel, iterations=1)
cv.imshow("dilate", img_dilate)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/JKuhVr
