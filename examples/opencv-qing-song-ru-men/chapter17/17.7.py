# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 代码解释 https://is.gd/SrUJ6f
# 运行结果 https://is.gd/pz5wM8

img = cv2.imread('lenacolor.png')

mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 400)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result = img * mask[:, :, np.newaxis]

cv2.rectangle(img, (50, 50), (450, 450), (255, 0, 0), 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.axis('off')

result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
plt.subplot(122), plt.imshow(result), plt.axis('off')

plt.show()
