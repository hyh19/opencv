import cv2

# 预加载分类器
face_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
nose_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_nose.xml')
mouth_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')

red = (0, 0, 255)  # 脸
green = (0, 255, 0)  # 眼
yellow = (0, 255, 255)  # 鼻
blue = (255, 0, 0)  # 嘴

# 存储分类器和颜色
classifiers = [eye_classifier, nose_classifier, mouth_classifier]
colors = [green, yellow, blue]


def detect(classifier, face_roi, face_x, face_y, color, img):
    res = classifier.detectMultiScale(face_roi, 1.1, 3)
    for x, y, w, h in res:
        x += face_x
        y += face_y
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)


img = cv2.imread('p3.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(img_gray, 1.1, 3)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), red, 2)
    face_roi = img_gray[y:y + h, x:x + w]
    # 使用列表循环来避免重复代码块
    for classifier, color in zip(classifiers, colors):
        detect(classifier, face_roi, x, y, color, img)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

# 运行结果 https://is.gd/5Jdm0R
