import cv2

img = cv2.imread('/Users/hyh/Downloads/IMG_8503.JPG')

# shape 属性中包括了三个信息
# 高度 长度 通道数
print(img.shape)

# 图像占用多大空间
# 高度 * 长度 * 通道数
print(img.size)

# 图像中每个元素的位深
print(img.dtype)
