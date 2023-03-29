import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 画线
cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5, 4)
cv2.line(img, (10, 100), (300, 480), (0, 0, 255), 5, 16)

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
