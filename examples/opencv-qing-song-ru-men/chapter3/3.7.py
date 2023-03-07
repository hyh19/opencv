# -*- coding: utf-8 -*-
import cv2
import numpy as np

a = np.random.randint(0, 255, (5, 5), dtype=np.uint8)
b = np.zeros((5, 5), dtype=np.uint8)
b[0:3, 0:3] = 255
b[4, 4] = 255
c = cv2.bitwise_and(a, b)
print("a=\n", a)
print("b=\n", b)
print("c=\n", c)
