# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

RECTANGLE = 1
CIRCLE = 2
LINE = 3
ELLIPSE = 4
TEXT = 5

mode = RECTANGLE
size = 400
thickness = -1


def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        point = np.random.randint(1, high=size - 50, size=(2,)).tolist()
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        if mode == RECTANGLE:
            cv.rectangle(img, (x, y), point, color, thickness)
        elif mode == CIRCLE:
            radius = np.random.randint(1, size / 5)
            cv.circle(img, (x, y), radius, color, thickness)
        elif mode == LINE:
            cv.line(img, point, (x, y), color, 3)
        elif mode == ELLIPSE:
            angle = np.random.randint(0, 361)
            cv.ellipse(img, (x, y), (100, 150), angle, 0, 360, color, thickness)
        elif mode == TEXT:
            cv.putText(img, 'OpenCV', (0, round(size / 2)), cv.FONT_HERSHEY_SIMPLEX, 2, color, 5)


img = np.ones((size, size, 3), np.uint8) * 255
win_name = 'win'
cv.namedWindow(win_name)
cv.setMouseCallback(win_name, draw)
while True:
    cv.imshow(win_name, img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('r'):
        mode = RECTANGLE
    elif k == ord('c'):
        mode = CIRCLE
    elif k == ord('l'):
        mode = LINE
    elif k == ord('e'):
        mode = ELLIPSE
    elif k == ord('t'):
        mode = TEXT
    elif k == ord('f'):
        thickness = -1
    elif k == ord('u'):
        thickness = 3
    elif k == 27:
        break
cv.destroyAllWindows()

# 运行结果 https://is.gd/raF6Sw
