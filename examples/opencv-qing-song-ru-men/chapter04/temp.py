import cv2 as cv
import numpy as np

bgr = cv.imread('opencv.jpg')
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
cv.imshow('bgr', bgr)

blue_range = (110, 130)
green_range = (50, 70)
red_range = (0, 30)
color_range_list = [blue_range, green_range, red_range]
color_name_list = ['blue', 'green', 'red']
for color_range, color_name in zip(color_range_list, color_name_list):
    lower, upper = color_range
    mask = cv.inRange(hsv, (lower, 50, 50), (upper, 255, 255))
    res = cv.bitwise_and(bgr, bgr, mask=mask)
    cv.imshow(color_name, res)

cv.waitKey()
cv.destroyAllWindows()
