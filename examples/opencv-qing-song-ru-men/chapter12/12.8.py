# -*- coding: utf-8 -*-
import cv2 as cv

o1 = cv.imread('cs1.bmp')
gray = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
HuM1 = cv.HuMoments(cv.moments(gray)).flatten()
print("cv.moments(gray)=\n", cv.moments(gray))
print("\nHuM1=\n", HuM1)
print("\ncv2.moments(gray)['nu20']+cv.moments(gray)['nu02']=%f+%f=%f\n"
      % (cv.moments(gray)['nu20'], cv.moments(gray)['nu02'],
         cv.moments(gray)['nu20'] + cv.moments(gray)['nu02']))
print("HuM1[0]=", HuM1[0])
print("\nHu[0]-(nu02+nu20)=",
      HuM1[0] - (cv.moments(gray)['nu20'] + cv.moments(gray)['nu02']))
