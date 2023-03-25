# -*- coding: utf-8 -*-
import numpy as np

img = np.random.randint(10, 99, size=[2, 4, 3], dtype=np.uint8)
print("img=\n", img)
print("读取像素点img[1,2,0]=", img.item(1, 2, 0))
print("读取像素点img[0,2,1]=", img.item(0, 2, 1))
print("读取像素点img[1,0,2]=", img.item(1, 0, 2))
img.itemset((1, 2, 0), 255)
img.itemset((0, 2, 1), 255)
img.itemset((1, 0, 2), 255)
print("修改后img=\n", img)
print("修改后像素点img[1,2,0]=", img.item(1, 2, 0))
print("修改后像素点img[0,2,1]=", img.item(0, 2, 1))
print("修改后像素点img[1,0,2]=", img.item(1, 0, 2))

"""
img=
 [[[87 43 90]
  [24 94 66]
  [48 88 31]
  [22 53 44]]

 [[25 65 83]
  [68 58 67]
  [74 77 65]
  [32 61 83]]]
读取像素点img[1,2,0]= 74
读取像素点img[0,2,1]= 88
读取像素点img[1,0,2]= 83
修改后img=
 [[[ 87  43  90]
  [ 24  94  66]
  [ 48 255  31]
  [ 22  53  44]]

 [[ 25  65 255]
  [ 68  58  67]
  [255  77  65]
  [ 32  61  83]]]
修改后像素点img[1,2,0]= 255
修改后像素点img[0,2,1]= 255
修改后像素点img[1,0,2]= 255
"""
