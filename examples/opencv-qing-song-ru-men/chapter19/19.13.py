# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("lena512.bmp", cv2.IMREAD_GRAYSCALE)
win_name = "win"
trackbar_type = "Type"
trackbar_value = "Value"
threshold_type = 0
threshold_value = 127


def on_change_type(pos):
    global threshold_type
    global threshold_value
    threshold_type = cv2.getTrackbarPos(trackbar_type, win_name)
    threshold_value = cv2.getTrackbarPos(trackbar_value, win_name)
    _, result = cv2.threshold(img, threshold_value, 255, threshold_type)
    cv2.imshow(win_name, result)


def on_change_value(pos):
    global threshold_type
    global threshold_value
    threshold_type = cv2.getTrackbarPos(trackbar_type, win_name)
    threshold_value = cv2.getTrackbarPos(trackbar_value, win_name)
    _, result = cv2.threshold(img, threshold_value, 255, threshold_type)
    cv2.imshow(win_name, result)


cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.imshow(win_name, img)
cv2.createTrackbar(trackbar_type, win_name, threshold_type, 4, on_change_type)
cv2.createTrackbar(trackbar_value, win_name, threshold_value, 255, on_change_value)
if cv2.waitKey() == 27:
    cv2.destroyAllWindows()
