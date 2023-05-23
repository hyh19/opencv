# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('cc.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

red = (0, 0, 255)
blue = (255, 0, 0)

_, contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, red, 2)

x, y, w, h = cv.boundingRect(contours[0])
cv.rectangle(img, (x, y), (x + w, y + h), blue, 3)
print(f'Aspect Ratio = {w / h}')

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/sTe9N8
