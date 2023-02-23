import cv2
import numpy as np

# 创建一张图片
img = np.zeros((200, 200), np.uint8)

img[20:120, 20:120] = 255

new_img = cv2.bitwise_not(img)

cv2.imshow('new_img', new_img)
cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
