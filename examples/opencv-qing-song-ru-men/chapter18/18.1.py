# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c == 27:  # ESC键
        break
cap.release()
cv2.destroyAllWindows()
