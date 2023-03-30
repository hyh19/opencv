# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/zsFe3G

size = 300
img = np.ones((size, size, 3), np.uint8) * 255
img = cv2.rectangle(img, (50, 50), (size - 100, size - 50), (0, 0, 255), -1)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
