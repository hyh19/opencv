# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('contours.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
hull1 = cv.convexHull(contours[0])
print(f'returnPoints = True: \n{hull1}')
hull2 = cv.convexHull(contours[0], returnPoints=False)
print(f'returnPoints = False: \n{hull2}')

'''
returnPoints = True: 
[[[195 270]]

 [[195 383]]

 [[ 79 383]]

 [[ 79 270]]]
returnPoints = False: 
[[3]
 [2]
 [1]
 [0]]
'''
