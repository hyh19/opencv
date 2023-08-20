# -*- coding: utf-8 -*-
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
# 注意：frameSize 要和摄像头分辨率一致
out = cv.VideoWriter('out.avi', fourcc, 20, (1280, 720))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break
cap.release()
out.release()
cv.destroyAllWindows()
