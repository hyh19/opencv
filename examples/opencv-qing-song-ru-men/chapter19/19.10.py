# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/A4GFTB

size = 400


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        px = np.random.randint(1, size - 50)
        py = np.random.randint(1, size - 50)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        cv2.rectangle(img, (x, y), (px, py), color, 2)


img = np.ones((size, size, 3), dtype="uint8") * 255
cv2.namedWindow('win')
cv2.setMouseCallback('win', draw)
while True:
    cv2.imshow('win', img)
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()
