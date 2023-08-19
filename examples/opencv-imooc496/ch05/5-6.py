import cv2 as cv
import numpy as np

# TODO 复习 8.18

cur_shape = 0
start_pos = (0, 0)

# 显示窗口和背景
img = np.zeros((480, 640, 3), np.uint8)


# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    # print(event, x, y, flags, userdata)
    global cur_shape, start_pos

    if event & cv.EVENT_LBUTTONDOWN == cv.EVENT_LBUTTONDOWN:
        start_pos = (x, y)
    elif event & cv.EVENT_LBUTTONUP == cv.EVENT_LBUTTONUP:
        if cur_shape == 0:  # draw line
            cv.line(img, start_pos, (x, y), (0, 0, 255))
        elif cur_shape == 1:  # draw rectangle
            cv.rectangle(img, start_pos, (x, y), (0, 0, 255))
        elif cur_shape == 2:  # draw circle
            a = x - start_pos[0]
            b = y - start_pos[1]
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv.circle(img, start_pos, r, (0, 0, 255))
        else:
            print('error: no shape')


# 创建窗口
cv.namedWindow('draw shape', cv.WINDOW_NORMAL)
# 设置鼠标回调
cv.setMouseCallback('draw shape', mouse_callback)

while True:
    cv.imshow('draw shape', img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):  # line
        cur_shape = 0
    elif key == ord('r'):  # rectangle
        cur_shape = 1
    elif key == ord('c'):  # circle
        cur_shape = 2

cv.destroyAllWindows()
