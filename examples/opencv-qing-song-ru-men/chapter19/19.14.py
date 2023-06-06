# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 400
img = np.ones((size, size, 3), np.uint8) * 255
win_name = 'win'
trackbar_fill = 'Fill'
thickness = 2


def change_thickness(pos):
    global thickness
    thickness = -1 if cv.getTrackbarPos(trackbar_fill, win_name) == 1 else 2


def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = np.random.randint(1, size - 50)
        y1 = np.random.randint(1, size - 50)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        cv.rectangle(img, (x, y), (x1, y1), color, thickness)
        cv.imshow(win_name, img)


cv.namedWindow(win_name)
cv.setMouseCallback(win_name, draw)
cv.createTrackbar(trackbar_fill, win_name, 0, 1, change_thickness)

while True:
    cv.imshow(win_name, img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

# 运行结果 https://is.gd/VoIj1q
