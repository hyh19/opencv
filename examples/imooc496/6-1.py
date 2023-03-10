import cv2
import numpy as np

dog = cv2.imread('dog.jpeg')

# print(dog.shape)

img = np.ones((1200, 1920, 3), np.uint8) * 50

cv2.imshow('dog', dog)

result = cv2.add(dog, img)
cv2.imshow('result', result)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
