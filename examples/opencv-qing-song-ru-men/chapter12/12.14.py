# -*- coding: utf-8 -*-
import cv2
import numpy as np

o = cv2.imread('cc.bmp')
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(binary,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)

rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n", rect)

points = cv2.boxPoints(rect)
print("\n转换后的points：\n", points)

points = np.int0(points)  # 取整
cv2.drawContours(o, [points], 0, (0, 0, 255), 2)
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()
