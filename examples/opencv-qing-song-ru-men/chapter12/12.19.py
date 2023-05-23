# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('cc.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 比例
scales = [0.1, 0.09, 0.055, 0.05, 0.02]
for scale in scales:
    canvas = img.copy()
    epsilon = scale * cv.arcLength(contours[0], True)
    approx = cv.approxPolyDP(contours[0], epsilon, True)
    canvas = cv.drawContours(canvas, [approx], 0, (0, 0, 255), 2)
    cv.imshow(f"epsilon = {epsilon}", canvas)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/6AgtrF
