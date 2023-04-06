# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/AiyDQM

image_names = ['cs.bmp', 'cs3.bmp', 'hand.bmp']
contours_list = []

for i, file_name in enumerate(image_names):
    img = cv.imread(file_name)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    _, contours, _ = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, 0, (0, 0, 255), 2)
    cv.imshow(f'img{i}', img)
    contours_list.append(contours[0])

shape_extractor = cv.createHausdorffDistanceExtractor()

d1 = shape_extractor.computeDistance(contours_list[0], contours_list[0])
print(f'与自身的距离 d1 = {d1}')
d2 = shape_extractor.computeDistance(contours_list[0], contours_list[1])
print(f'与旋转缩放后对象的距离 d2 = {d2}')
d3 = shape_extractor.computeDistance(contours_list[0], contours_list[2])
print(f'与不相似对象的距离 d3 = {d3}')

cv.waitKey()
cv.destroyAllWindows()
