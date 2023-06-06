# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread("lena512.bmp", cv.IMREAD_GRAYSCALE)
win_name = "win"
trackbar_type = "Threshold Type"
trackbar_value = "Threshold Value"


def change_thresh(pos):
    threshold_type = cv.getTrackbarPos(trackbar_type, win_name)
    threshold_value = cv.getTrackbarPos(trackbar_value, win_name)
    _, img_thresh = cv.threshold(img_gray, threshold_value, 255, threshold_type)
    cv.imshow(win_name, img_thresh)


cv.namedWindow(win_name, cv.WINDOW_NORMAL)
cv.imshow(win_name, img_gray)
cv.createTrackbar(trackbar_type, win_name, 0, 4, change_thresh)
cv.createTrackbar(trackbar_value, win_name, 127, 255, change_thresh)
if cv.waitKey() == 27:
    cv.destroyAllWindows()
