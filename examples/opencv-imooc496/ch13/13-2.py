import cv2

# 运行结果 https://is.gd/5Jdm0R

img = cv2.imread('p3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
mouth = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')
nose = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_nose.xml')

blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)


def detect(classifier, the_face_roi, the_face_x, the_face_y, color):
    res = classifier.detectMultiScale(the_face_roi, 1.1, 3)
    for (x, y, w, h) in res:
        x += the_face_x
        y += the_face_y
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)


face_result = face.detectMultiScale(gray, 1.1, 3)
for (face_x, face_y, face_w, face_h) in face_result:
    cv2.rectangle(img, (face_x, face_y), (face_x + face_w, face_y + face_h), red, 2)
    face_roi = gray[face_y:face_y + face_h, face_x:face_x + face_w]
    detect(eye, face_roi, face_x, face_y, green)
    detect(nose, face_roi, face_x, face_y, yellow)
    detect(mouth, face_roi, face_x, face_y, blue)

cv2.imshow('img', img)
cv2.waitKey()
