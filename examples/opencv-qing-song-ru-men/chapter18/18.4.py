# -*- coding: utf-8 -*-
import cv2 as cv

cap = cv.VideoCapture('viptrain.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.Canny(frame, 100, 200)
    cv.imshow('frame', frame)
    if cv.waitKey(33) == 27:  # ESC键
        break
cap.release()
cv.destroyAllWindows()
