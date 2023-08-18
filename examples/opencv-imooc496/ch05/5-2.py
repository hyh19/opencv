import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画矩形
cv.rectangle(img, pt1=(10, 10), pt2=(100, 100), color=(255, 0, 0), thickness=cv.FILLED)

# 画圆
cv.circle(img, center=(320, 240), radius=100, color=(0, 0, 255))
cv.circle(img, center=(320, 240), radius=10, color=(0, 255, 0), thickness=cv.FILLED)

cv.imshow('draw', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
