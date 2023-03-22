# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

a = cv.imread("lenacolor.png", cv.IMREAD_UNCHANGED)
cv.imshow("original", a)
face = np.random.randint(0, 256, (180, 100, 3))
a[220:400, 250:350] = face
cv.imshow("result", a)
cv.waitKey()
cv.destroyAllWindows()
