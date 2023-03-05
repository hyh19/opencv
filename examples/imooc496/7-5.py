import cv2

dog = cv2.imread('./dog.jpeg')
h, w, ch = dog.shape

print(dog.shape)

# 旋转方向是逆时针，中心点是 (x, y)
M = cv2.getRotationMatrix2D((w / 2, h / 2), 15, 1.0)

# 如果想改变新图像的尺寸，需要修改 dsize
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('dog', dog)
cv2.imshow('new', new)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# getRotationMatrix2D: https://t.ly/1g6M
