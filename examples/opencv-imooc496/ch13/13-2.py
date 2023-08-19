import cv2 as cv

img = cv.imread('p3.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 预加载分类器
face_classifier = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')
nose_classifier = cv.CascadeClassifier('haarcascades/haarcascade_mcs_nose.xml')
mouth_classifier = cv.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')

red = (0, 0, 255)  # 脸
green = (0, 255, 0)  # 眼
yellow = (0, 255, 255)  # 鼻
blue = (255, 0, 0)  # 嘴

# 存储分类器和颜色
classifiers = [eye_classifier, nose_classifier, mouth_classifier]
colors = [green, yellow, blue]


def detect(classifier, face_roi, face_x, face_y, color, img):
    objects = classifier.detectMultiScale(face_roi, scaleFactor=1.1, minNeighbors=3)
    for x, y, w, h in objects:
        x += face_x
        y += face_y
        cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=color, thickness=2)


faces = face_classifier.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3)
for x, y, w, h in faces:
    cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=red, thickness=2)
    face_roi = img_gray[y:y + h, x:x + w]
    # 使用列表循环来避免重复代码块
    for classifier, color in zip(classifiers, colors):
        detect(classifier, face_roi, x, y, color, img)

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/5Jdm0R
