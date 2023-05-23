# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('cc.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

red = (0, 0, 255)
blue = (255, 0, 0)

_, contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, red, 2)
cnt_area = cv.contourArea(contours[0])

equivalent_diameter = np.sqrt(4 * cnt_area / np.pi)
print(f'Equivalent Diameter = {equivalent_diameter}')
cv.circle(img, (100, 100), int(equivalent_diameter / 2), blue, 3)

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/xdRvXa
