# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('dface3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_classifier.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5)
)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
