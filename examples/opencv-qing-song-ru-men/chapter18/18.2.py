# -*- coding: utf-8 -*-
import cv2 as cv

cap = cv.VideoCapture('viptrain.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('frame', frame)
    # 视频的帧率是 30，帧与帧的时间间隔是 1000 / 30 = 33。
    c = cv.waitKey(33)
    if c == 27:
        break
cap.release()
cv.destroyAllWindows()
