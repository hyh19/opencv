# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr_img = np.random.randint(0, 256, size=(2, 3, 3), dtype=np.uint8)
bgra_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2BGRA)
print(f'bgr = \n{bgr_img}')
print(f'bgra = \n{bgra_img}')

blue_img, green_img, red_img, alpha_img = cv.split(bgra_img)
print(f'alpha = \n{alpha_img}')

alpha_img[:, :] = 125
bgra_img = cv.merge([blue_img, green_img, red_img, alpha_img])
print(f'bgra = \n{bgra_img}')

'''
bgr = 
[[[ 83 186 155]
  [  2  22 175]
  [196 225 236]]

 [[ 52 155  27]
  [128  96 201]
  [ 91  54 147]]]
bgra = 
[[[ 83 186 155 255]
  [  2  22 175 255]
  [196 225 236 255]]

 [[ 52 155  27 255]
  [128  96 201 255]
  [ 91  54 147 255]]]
alpha = 
[[255 255 255]
 [255 255 255]]
bgra = 
[[[ 83 186 155 125]
  [  2  22 175 125]
  [196 225 236 125]]

 [[ 52 155  27 125]
  [128  96 201 125]
  [ 91  54 147 125]]]
'''
