# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = np.random.randint(0, 256, size=[512, 512], dtype=np.uint8)
cv2.imshow("demo", img)
cv2.waitKey()
cv2.destroyAllWindows()
