import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# 绘制文本
cv.putText(img, "Hello OpenCV!", org=(10, 400), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(255, 0, 0))

cv.imshow('draw', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
