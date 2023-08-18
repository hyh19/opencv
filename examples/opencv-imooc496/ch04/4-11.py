import cv2 as cv

img = cv.imread('../images/RMB.jpeg')

# shape 属性中包括了三个信息
# 高度（行） 宽度（列） 通道数
print(img.shape)

# 图像占用多大空间
# 高度（行） * 宽度（列） * 通道数
print(img.size)

# 图像中每个元素的位深
print(img.dtype)
