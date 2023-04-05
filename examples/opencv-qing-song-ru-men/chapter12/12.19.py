# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/6AgtrF

img = cv.imread('cc.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 比例
scales = [0.1, 0.09, 0.055, 0.05, 0.02]
for scale in scales:
    temp = img.copy()
    epsilon = scale * cv.arcLength(contours[0], True)
    approx = cv.approxPolyDP(contours[0], epsilon, True)
    temp = cv.drawContours(temp, [approx], 0, (0, 0, 255), 2)
    cv.imshow(f"epsilon = {epsilon}", temp)

cv.waitKey()
cv.destroyAllWindows()
