# -*- coding: utf-8 -*-
import cv2 as cv

kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
kernel2 = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
print('kernel1=\n', kernel1)
print('kernel2=\n', kernel2)
print('kernel3=\n', kernel3)
