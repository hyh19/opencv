import cv2 as cv
import numpy as np

dog = cv.imread('../images/dog.jpeg')
img = np.ones(dog.shape, np.uint8) * 50

result = cv.subtract(dog, img)

cv.imshow('dog', dog)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
