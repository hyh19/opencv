# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = np.random.randint(0, 256, size=[2, 3, 3], dtype=np.uint8)
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print("img=\n", img)
print("bgra=\n", bgra)
b, g, r, a = cv2.split(bgra)
print("a=\n", a)
a[:, :] = 125
bgra = cv2.merge([b, g, r, a])
print("bgra=\n", bgra)
