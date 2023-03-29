# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 运行结果 https://is.gd/hc1pTn

img = cv2.imread('lenacolor.png')
img_mask = cv2.imread('mask.png')
img_mask_gray = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)

mask = np.zeros(img.shape[:2], np.uint8)
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 500)

# 第一次处理 GC_INIT_WITH_RECT
cv2.grabCut(img, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)
mask1 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result1 = img * mask1[:, :, np.newaxis]

mask[img_mask_gray == 0] = 0
mask[img_mask_gray == 255] = 1

# 第二次处理 GC_INIT_WITH_MASK
cv2.grabCut(img, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result2 = img * mask2[:, :, np.newaxis]

cv2.rectangle(img, (50, 50), (450, 450), (255, 0, 0), 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(221), plt.imshow(img), plt.axis('off'), plt.title('img')

result1 = cv2.cvtColor(result1, cv2.COLOR_BGR2RGB)
plt.subplot(222), plt.imshow(result1), plt.axis('off'), plt.title('result1')

img_mask = cv2.cvtColor(img_mask, cv2.COLOR_BGR2RGB)
plt.subplot(223), plt.imshow(img_mask), plt.axis('off'), plt.title('img_mask')

result2 = cv2.cvtColor(result2, cv2.COLOR_BGR2RGB)
plt.subplot(224), plt.imshow(result2), plt.axis('off'), plt.title('result2')

plt.show()
