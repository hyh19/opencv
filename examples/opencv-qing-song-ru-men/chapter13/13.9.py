# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

mask = np.zeros([600, 600], np.uint8)
mask[200:400, 200:400] = 255
cv.imshow('mask', mask)
cv.waitKey()
cv.destroyAllWindows()
