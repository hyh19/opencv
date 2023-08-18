import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

roi = img[100:400, 100:600]

example = 2
if example == 0:
    roi[:, :] = [0, 0, 255]
    # roi[:] = [0, 0, 255]
elif example == 1:
    roi[:, 50] = [0, 0, 255]
elif example == 2:
    roi[10:200, 10:200] = [0, 255, 0]

cv.imshow('img', roi)
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
