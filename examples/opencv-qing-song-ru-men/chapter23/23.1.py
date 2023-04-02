# -*- coding: utf-8 -*-
import cv2

# 图像预处理
img = cv2.imread('dface3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸检测
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = classifier.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5)
)

# 绘制人脸矩形
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)

# 显示图像并释放资源
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
