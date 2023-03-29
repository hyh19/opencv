import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画矩形
cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 255), -1)

# 画圆
cv2.circle(img, (320, 240), 100, (0, 0, 255))
cv2.circle(img, (320, 240), 5, (0, 0, 255), -1)

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
