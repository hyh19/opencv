import cv2
import numpy as np

dog = cv2.imread('images/dog.jpeg')
h, w, ch = dog.shape
print(dog.shape)

M = np.float32([[1, 0, 500], [0, 1, 300]])
# 如果想改变新图像的尺寸，需要修改 dsize
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('dog', dog)
cv2.imshow('new', new)

cv2.waitKey(0)
cv2.destroyAllWindows()

# warpAffine: https://t.ly/7J_l
