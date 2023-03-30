# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (1280, 720))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
