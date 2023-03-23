# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, param1=50, param2=30, minRadius=100, maxRadius=200)
circles = np.uint16(np.around(circles))

res = img.copy()
for i in circles[0, :]:
    cv2.circle(res, (i[0], i[1]), i[2], (255, 0, 0), 12)
    cv2.circle(res, (i[0], i[1]), 5, (0, 0, 255), 12)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
res_rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img_rgb), plt.axis('off')
plt.subplot(122), plt.imshow(res_rgb), plt.axis('off')
plt.show()
