import cv2 as cv

# 运行结果 https://is.gd/wK6glU

face_classifier = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
img = cv.imread('p3.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.1, 3)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()