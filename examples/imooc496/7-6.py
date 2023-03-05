import cv2
import numpy as np

dog = cv2.imread('./dog.jpeg')
h, w, ch = dog.shape

print(dog.shape)

src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])
M = cv2.getAffineTransform(src, dst)

# 如果想改变新图像的尺寸，需要修改 dsize
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('dog', dog)
cv2.imshow('new', new)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# getAffineTransform: https://t.ly/deh5
