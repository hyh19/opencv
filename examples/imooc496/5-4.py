import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画多边形
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
# cv2.polylines(img, [pts], True, (0, 0, 255))

# 填充多边形
cv2.fillPoly(img, [pts], (255, 255, 0))

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
