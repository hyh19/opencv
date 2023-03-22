# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[256, 256, 3], dtype=np.uint8)
cv.imshow("demo", img)
cv.waitKey()
cv.destroyAllWindows()
