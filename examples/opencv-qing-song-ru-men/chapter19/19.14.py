# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/VoIj1q

size = 400
img = np.ones((size, size, 3), np.uint8) * 255
win_name = 'win'
trackbar_name = 'Fill'
thickness = -1


def fill(pos):
    pass


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        px = np.random.randint(1, size - 50)
        py = np.random.randint(1, size - 50)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        cv2.rectangle(img, (x, y), (px, py), color, thickness)


cv2.namedWindow(win_name)
cv2.setMouseCallback(win_name, draw)
cv2.createTrackbar(trackbar_name, win_name, 0, 1, fill)
while True:
    cv2.imshow(win_name, img)
    mode = cv2.getTrackbarPos(trackbar_name, win_name)
    if mode == 0:
        thickness = 2
    else:
        thickness = -1
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
