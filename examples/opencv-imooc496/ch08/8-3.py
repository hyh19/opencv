import cv2 as cv
import numpy as np

img = cv.imread('../images/dog.jpeg')

kernel = np.ones((5, 5), np.float32) / 25
result = cv.filter2D(img, ddepth=-1, kernel=kernel)

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# filter2D: https://t.ly/COoA
