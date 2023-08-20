# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 400


def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = np.random.randint(1, size - 50)
        y1 = np.random.randint(1, size - 50)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        cv.rectangle(img, (x, y), (x1, y1), color, 2)


img = np.ones((size, size, 3), dtype="uint8") * 255
win_name = 'win'
cv.namedWindow(win_name)
cv.setMouseCallback(win_name, draw)
while True:
    cv.imshow(win_name, img)
    if cv.waitKey(20) == 27:
        break
cv.destroyAllWindows()

# 运行结果 https://is.gd/A4GFTB
