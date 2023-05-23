# -*- coding: utf-8 -*-
import cv2 as cv

image_names = ['cs.bmp', 'cs3.bmp', 'hand.bmp']
contours_list = []

for i, file_name in enumerate(image_names):
    img = cv.imread(file_name)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
    _, contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, 0, (0, 0, 255), 2)
    cv.imshow(f'img{i}', img)
    contours_list.append(contours[0])

for dist_extractor in [cv.createShapeContextDistanceExtractor(), cv.createHausdorffDistanceExtractor()]:
    print(f'{dist_extractor.__class__.__name__}:')
    d1 = dist_extractor.computeDistance(contours_list[0], contours_list[0])
    print(f'与自身的距离 d1 = {d1}')
    d2 = dist_extractor.computeDistance(contours_list[0], contours_list[1])
    print(f'与旋转缩放后对象的距离 d2 = {d2}')
    d3 = dist_extractor.computeDistance(contours_list[0], contours_list[2])
    print(f'与不相似对象的距离 d3 = {d3}')

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/AiyDQM
