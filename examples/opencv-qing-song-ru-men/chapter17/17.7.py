# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv as cv
import matplotlib.pyplot as plt

img = cv.imread('lenacolor.png')

mask = np.zeros(img.shape[:2], np.uint8)
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 400)

cv.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv.GC_INIT_WITH_RECT)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result = img * mask[:, :, np.newaxis]

cv.rectangle(img, (50, 50), (450, 450), (255, 0, 0), 3)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.axis('off')

result = cv.cvtColor(result, cv.COLOR_BGR2RGB)
plt.subplot(122), plt.imshow(result), plt.axis('off')

plt.show()

# 运行结果 https://is.gd/pz5wM8
