# -*- coding: utf-8 -*-
import cv2 as cv

cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('frame', frame)
    c = cv.waitKey(1)
    if c == 27:  # 按 esc 键关闭窗口
        break
cap.release()
cv.destroyAllWindows()
