# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture('viptrain.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.Canny(frame, 100, 200)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:  # ESC键
        break
cap.release()
cv2.destroyAllWindows()
