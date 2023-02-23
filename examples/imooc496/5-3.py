import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画圆
cv2.circle(img, (320, 240), 100, (0, 0, 255))
cv2.circle(img, (320, 240), 5, (0, 0, 255), -1)

# 画椭圆
# 度是按顺时针计算的
cv2.ellipse(img, (320, 240), (100, 50), 0, 90, 315, (255, 0, 0), 1)

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
