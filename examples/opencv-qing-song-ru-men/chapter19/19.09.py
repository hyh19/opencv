# -*- coding: utf-8 -*-
import cv2
import numpy as np


def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("单击了鼠标右键")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("单击了中间键")
    elif flags == cv2.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")


img = np.ones((300, 300, 3), np.uint8) * 255
cv2.namedWindow('win')
cv2.setMouseCallback('win', on_mouse)
cv2.imshow('win', img)
cv2.waitKey()
cv2.destroyAllWindows()
