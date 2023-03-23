# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('computer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 160, minLineLength=100, maxLineGap=10)

res = img.copy()
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(res, (x1, y1), (x2, y2), (255, 0, 0), 2)

plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.axis('off')
plt.subplot(122), plt.imshow(cv.cvtColor(res, cv.COLOR_BGR2RGB)), plt.axis('off')
plt.show()
