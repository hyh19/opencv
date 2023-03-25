# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3lyIJ52

img = np.random.randint(0, 256, size=[512, 512], dtype=np.uint8)
cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
