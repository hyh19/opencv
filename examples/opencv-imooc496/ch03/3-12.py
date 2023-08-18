import cv2 as cv
import numpy as np


def callback(x):
    pass


# 创建窗口
cv.namedWindow('trackbar', cv.WINDOW_NORMAL)

# 创建 trackbar
cv.createTrackbar('R', 'trackbar', 0, 255, callback)
cv.createTrackbar('G', 'trackbar', 0, 255, callback)
cv.createTrackbar('B', 'trackbar', 0, 255, callback)

# 创建一张背景图片
img = np.zeros((480, 640, 3), np.uint8)

while True:
    # 获取当前 trackbar 的值
    r = cv.getTrackbarPos('R', 'trackbar')
    g = cv.getTrackbarPos('G', 'trackbar')
    b = cv.getTrackbarPos('B', 'trackbar')

    # 改变背景图片颜色
    img[:] = [b, g, r]
    cv.imshow('trackbar', img)

    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
