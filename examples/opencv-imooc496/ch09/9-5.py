import cv2 as cv
import numpy as np

img = cv.imread('../images/j.png')

kernel = np.ones((3, 3), np.uint8)
dst = cv.erode(img, kernel, iterations=1)

cv.imshow('img', img)
cv.imshow('dst', dst)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# erode: https://t.ly/3GTc
