# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/UFkfz9

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255
pts = np.array([[200, 50], [300, 200], [200, 350], [100, 200]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 0), 8)
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
