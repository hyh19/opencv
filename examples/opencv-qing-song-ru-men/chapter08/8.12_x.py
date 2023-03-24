# -*- coding: utf-8 -*-
import cv2 as cv

rect = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
cross = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
print('rect=\n', rect)
print('cross=\n', cross)
print('ellipse=\n', ellipse)
