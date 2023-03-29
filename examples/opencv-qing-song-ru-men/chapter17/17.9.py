# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 运行结果 https://is.gd/0Tphux

img = cv2.imread('lenacolor.png')

bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)
mask = np.zeros(img.shape[:2], np.uint8)
mask[30:512, 50:400] = 3
mask[50:300, 150:200] = 1

cv2.grabCut(img, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result = img * mask[:, :, np.newaxis]

# (x, y) = (col, row)
cv2.rectangle(img, (50, 30), (400, 512), (255, 0, 0), 3)
cv2.rectangle(img, (150, 50), (200, 300), (0, 0, 255), 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.axis('off'), plt.title('img')

result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
plt.subplot(122), plt.imshow(result), plt.axis('off'), plt.title('result')

plt.show()
