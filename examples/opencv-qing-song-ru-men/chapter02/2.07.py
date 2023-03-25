# -*- coding: utf-8 -*-
import numpy as np

img = np.random.randint(10, 99, size=[5, 5], dtype=np.uint8)
print("img=\n", img)
print("读取像素点img.item(3,2)=", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后img=\n", img)
print("修改后像素点img.item(3,2)=", img.item(3, 2))

"""
img=
 [[89 81 50 74 66]
 [95 75 79 77 58]
 [36 10 24 49 54]
 [36 36 66 35 62]
 [14 71 69 57 15]]
读取像素点img.item(3,2)= 66
修改后img=
 [[ 89  81  50  74  66]
 [ 95  75  79  77  58]
 [ 36  10  24  49  54]
 [ 36  36 255  35  62]
 [ 14  71  69  57  15]]
修改后像素点img.item(3,2)= 255
"""
