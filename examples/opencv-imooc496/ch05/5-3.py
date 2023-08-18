import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画圆
cv.circle(img, center=(320, 240), radius=100, color=(0, 0, 255))
cv.circle(img, center=(320, 240), radius=10, color=(0, 0, 255), thickness=cv.FILLED)

# 画椭圆
# 度是按顺时针计算的
cv.ellipse(img, center=(320, 240), axes=(100, 50), angle=0, startAngle=90, endAngle=315, color=(255, 0, 0), thickness=1)

cv.imshow('draw', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
