import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画线
cv.line(img, pt1=(10, 20), pt2=(300, 400), color=(0, 0, 255), thickness=5, lineType=cv.LINE_4)
cv.line(img, pt1=(10, 100), pt2=(300, 480), color=(255, 0, 0), thickness=5, lineType=cv.LINE_AA)

cv.imshow('draw', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
