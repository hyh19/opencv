# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 读取图像并灰度化
images = [cv.imread(f"e0{i}.png", cv.IMREAD_GRAYSCALE) for i in range(1, 3)]
images += [cv.imread(f"e1{i}.png", cv.IMREAD_GRAYSCALE) for i in range(1, 3)]
labels = [0, 0, 1, 1]

# 训练人脸识别器
recognizer = cv.face.EigenFaceRecognizer_create()
recognizer.train(images, np.array(labels))

# 预测新图像
predict_image = cv.imread("eTest.png", cv.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)

# 输出预测结果
print(f"label = {label}, confidence = {confidence}")
