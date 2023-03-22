# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv

img = np.random.randint(0, 256, size=[512, 512], dtype=np.uint8)
cv.imshow("demo", img)
cv.waitKey()
cv.destroyAllWindows()
