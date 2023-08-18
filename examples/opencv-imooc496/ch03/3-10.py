import cv2 as cv
import numpy as np


# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


# 创建窗口
cv.namedWindow('mouse', cv.WINDOW_NORMAL)
cv.resizeWindow('mouse', 640, 360)

# 设置鼠标回调
cv.setMouseCallback('mouse', mouse_callback, "123")

# 显示窗口和背景
img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv.imshow('mouse', img)
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
