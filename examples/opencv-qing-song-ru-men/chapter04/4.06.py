# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

blue_bgr = np.zeros((1, 1, 3), dtype=np.uint8)
blue_bgr[0, 0, 0] = 255
blue_hsv = cv.cvtColor(blue_bgr, cv.COLOR_BGR2HSV)
print(f'blue_bgr = {blue_bgr}')
print(f'blue_hsv = {blue_hsv}')

green_bgr = np.zeros((1, 1, 3), dtype=np.uint8)
green_bgr[0, 0, 1] = 255
green_hsv = cv.cvtColor(green_bgr, cv.COLOR_BGR2HSV)
print(f'green_bgr = {green_bgr}')
print(f'green_hsv = {green_hsv}')

red_bgr = np.zeros((1, 1, 3), dtype=np.uint8)
red_bgr[0, 0, 2] = 255
red_hsv = cv.cvtColor(red_bgr, cv.COLOR_BGR2HSV)
print(f'red_bgr = {red_bgr}')
print(f'red_hsv = {red_hsv}')

'''
blue_bgr = [[[255   0   0]]]
blue_hsv = [[[120 255 255]]]
green_bgr = [[[  0 255   0]]]
green_hsv = [[[ 60 255 255]]]
red_bgr = [[[  0   0 255]]]
red_hsv = [[[  0 255 255]]]
'''
