# -*- coding: utf-8 -*-
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena512g.bmp', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('temp.bmp', cv2.IMREAD_GRAYSCALE)
tw, th = template.shape[::-1]

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img, topLeft, bottomRight, 255, 2)

plt.subplot(121), plt.imshow(result, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

plt.show()
