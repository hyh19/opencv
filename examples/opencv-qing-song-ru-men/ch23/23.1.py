# -*- coding: utf-8 -*-
import cv2 as cv

# 图像预处理
img = cv.imread('dface3.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 人脸检测
classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = classifier.detectMultiScale(
    img_gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5)
)

# 绘制人脸矩形
for x, y, w, h in faces:
    cv.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)

# 显示图像并释放资源
cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/lNQO4M
