# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv as cv
import matplotlib.pyplot as plt

img = cv.imread('lenacolor.png')
img_mask = cv.imread('mask.png')
img_mask_gray = cv.cvtColor(img_mask, cv.COLOR_BGR2GRAY)

mask = np.zeros(img.shape[:2], np.uint8)
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 500)

# 第一次处理 GC_INIT_WITH_RECT
cv.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv.GC_INIT_WITH_RECT)
mask1 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result1 = img * mask1[:, :, np.newaxis]

mask[img_mask_gray == 0] = 0
mask[img_mask_gray == 255] = 1

# 第二次处理 GC_INIT_WITH_MASK
cv.grabCut(img, mask, None, bgd_model, fgd_model, 5, cv.GC_INIT_WITH_MASK)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result2 = img * mask2[:, :, np.newaxis]

cv.rectangle(img, (50, 50), (450, 450), (255, 0, 0), 3)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(221), plt.imshow(img), plt.axis('off'), plt.title('img')

result1 = cv.cvtColor(result1, cv.COLOR_BGR2RGB)
plt.subplot(222), plt.imshow(result1), plt.axis('off'), plt.title('result1')

img_mask = cv.cvtColor(img_mask, cv.COLOR_BGR2RGB)
plt.subplot(223), plt.imshow(img_mask), plt.axis('off'), plt.title('img_mask')

result2 = cv.cvtColor(result2, cv.COLOR_BGR2RGB)
plt.subplot(224), plt.imshow(result2), plt.axis('off'), plt.title('result2')

plt.show()

# 运行结果 https://is.gd/hc1pTn
