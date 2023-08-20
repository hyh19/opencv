# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def on_mouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event == cv.EVENT_RBUTTONDOWN:
        print("单击了鼠标右键")
    elif event == cv.EVENT_MBUTTONDOWN:
        print("单击了中间键")
    elif flags == cv.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")


img = np.ones((300, 300, 3), np.uint8) * 255
win_name = 'win'
cv.namedWindow(win_name)
cv.setMouseCallback(win_name, on_mouse)
cv.imshow(win_name, img)
cv.waitKey()
cv.destroyAllWindows()
