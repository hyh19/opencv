# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/6HWywx

size = 400
img = np.ones((size, size, 3), dtype="uint8") * 255
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0, 200), font, 3, (0, 0, 255), 15)
cv2.putText(img, 'OpenCV', (0, 200), font, 3, (0, 255, 0), 5)
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
