# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/xdRvXa

img = cv.imread('cc.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, (0, 0, 255), 2)
cnt_area = cv.contourArea(contours[0])
equivalent_diameter = np.sqrt(4 * cnt_area / np.pi)
print(f'equivalent_diameter = {equivalent_diameter}')
cv.circle(img, (100, 100), int(equivalent_diameter / 2), (255, 0, 0), 3)
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
