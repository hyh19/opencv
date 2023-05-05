# -*- coding: utf-8 -*-
import numpy as np

img = np.random.randint(10, 99, size=(5, 5), dtype=np.uint8)
print(f'img = \n{img}')
print(f'读取像素点 img.item(3,2) = {img.item(3, 2)}')
img.itemset((3, 2), 255)
print(f'修改后 img = \n{img}')
print(f'修改后像素点 img.item(3,2) = {img.item(3, 2)}')

'''
img = 
[[35 22 40 25 35]
 [26 41 90 12 77]
 [89 11 74 63 30]
 [53 81 35 12 72]
 [50 27 33 68 87]]
读取像素点 img.item(3,2) = 35
修改后 img = 
[[ 35  22  40  25  35]
 [ 26  41  90  12  77]
 [ 89  11  74  63  30]
 [ 53  81 255  12  72]
 [ 50  27  33  68  87]]
修改后像素点 img.item(3,2) = 255
'''
