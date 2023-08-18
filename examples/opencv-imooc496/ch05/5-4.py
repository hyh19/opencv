import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)

example = 1
if example == 0:
    # 画多边形
    cv.polylines(img, [pts], isClosed=True, color=(0, 0, 255))
elif example == 1:
    # 填充多边形
    cv.fillPoly(img, [pts], color=(255, 255, 0))

cv.imshow('draw', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
