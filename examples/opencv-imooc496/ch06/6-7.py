import cv2 as cv
import numpy as np

# 导入图片
dog = cv.imread('../images/dog.jpeg')

# 选择 dog 添加 logo 的位置
roi = dog[0:200, 0:200]
cv.imshow('roi', roi)

# 创建 logo
logo = np.zeros((200, 200, 3), np.uint8)
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]
cv.imshow('logo', logo)

# 创建 mask
mask = np.full((200, 200), 255, np.uint8)
mask[20:120, 20:120] = 0
mask[80:180, 80:180] = 0
cv.imshow('mask', mask)

# 抠出 logo 的位置（核心代码）
roi_mask = cv.bitwise_and(roi, roi, mask=mask)
cv.imshow('roi_mask', roi_mask)

roi_logo = cv.add(roi_mask, logo)
cv.imshow('roi_logo', roi_logo)

dog[0:200, 0:200] = roi_logo
cv.imshow('dog', dog)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
