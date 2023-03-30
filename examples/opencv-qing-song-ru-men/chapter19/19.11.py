# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/raF6Sw

size = 400
mode = 1
thickness = -1


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        radius = np.random.randint(1, size / 5)
        angle = np.random.randint(0, 361)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        a = np.random.randint(1, size - 50)
        if mode == 1:
            cv2.rectangle(img, (x, y), (a, a), color, thickness)
        elif mode == 2:
            cv2.circle(img, (x, y), radius, color, thickness)
        elif mode == 3:
            cv2.line(img, (a, a), (x, y), color, 3)
        elif mode == 4:
            cv2.ellipse(img, (x, y), (100, 150), angle, 0, 360, color, thickness)
        elif mode == 5:
            cv2.putText(img, 'OpenCV', (0, round(size / 2)), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 5)


img = np.ones((size, size, 3), np.uint8) * 255
cv2.namedWindow('win')
cv2.setMouseCallback('win', draw)
while True:
    cv2.imshow('win', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        mode = 1
    elif k == ord('c'):
        mode = 2
    elif k == ord('l'):
        mode = 3
    elif k == ord('e'):
        mode = 4
    elif k == ord('t'):
        mode = 5
    elif k == ord('f'):
        thickness = -1
    elif k == ord('u'):
        thickness = 3
    elif k == 27:
        break
cv2.destroyAllWindows()
