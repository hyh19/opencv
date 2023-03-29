import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 绘制文本
cv2.putText(img, "Hello World!", (10, 400), cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 0))

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
