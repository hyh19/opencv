# -*- coding: utf-8 -*-
import numpy as np

a = np.zeros((5, 5), dtype=np.uint8)
for _ in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1
print(f'a = \n{a}')
print(f'a 内非零值的坐标 = \n{np.transpose(np.nonzero(a))}')

'''
a = 
[[0 0 0 1 0]
 [1 0 0 0 0]
 [1 1 1 0 0]
 [0 1 1 0 0]
 [1 0 0 1 0]]
a 内非零值的坐标 = 
[[0 3]
 [1 0]
 [2 0]
 [2 1]
 [2 2]
 [3 1]
 [3 2]
 [4 0]
 [4 3]]
'''
