import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

b, g, r = cv.split(img)

b[10:100, 10:100] = 255
g[10:100, 10:100] = 255

img_merge = cv.merge((b, g, r))

cv.imshow('img', img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('img_merge', img_merge)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
