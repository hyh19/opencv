import cv2
import numpy as np

cur_shape = 0
start_pos = (0, 0)

# 显示窗口和背景
img = np.zeros((480, 640, 3), np.uint8)


# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    # print(event, x, y, flags, userdata)
    global cur_shape, start_pos

    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        start_pos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        if cur_shape == 0:  # draw line
            cv2.line(img, start_pos, (x, y), (0, 0, 255))
        elif cur_shape == 1:  # draw rectangle
            cv2.rectangle(img, start_pos, (x, y), (0, 0, 255))
        elif cur_shape == 2:  # draw circle
            a = x - start_pos[0]
            b = y - start_pos[1]
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv2.circle(img, start_pos, r, (0, 0, 255))
        else:
            print('error: no shape')


# 创建窗口
cv2.namedWindow('draw shape', cv2.WINDOW_NORMAL)
# 设置鼠标回调
cv2.setMouseCallback('draw shape', mouse_callback)

while True:
    cv2.imshow('draw shape', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):  # line
        cur_shape = 0
    elif key == ord('r'):  # rectangle
        cur_shape = 1
    elif key == ord('c'):  # circle
        cur_shape = 2

cv2.destroyAllWindows()
