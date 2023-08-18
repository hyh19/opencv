import cv2 as cv
import numpy as np

# 创建 logo
logo = np.zeros((200, 200, 3), np.uint8)
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]
cv.imshow('logo', logo)

# 创建 mask
mask = np.zeros((200, 200), np.uint8)
mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255
cv.imshow('mask', mask)

# 对 mask 按位求反
mask_not = cv.bitwise_not(mask)
cv.imshow('mask_not', mask_not)

# 导入图片
dog = cv.imread('../images/dog.jpeg')

# 选择 dog 添加 logo 的位置
roi = dog[0:200, 0:200]
cv.imshow('roi', roi)

# 抠出 logo 的位置
tmp = cv.bitwise_and(roi, roi, mask=mask_not)
cv.imshow('tmp', tmp)

dst = cv.add(tmp, logo)
dog[0:200, 0:200] = dst
cv.imshow('dst', dst)

cv.imshow('dog', dog)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
