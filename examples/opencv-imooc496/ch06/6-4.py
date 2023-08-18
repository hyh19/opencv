import cv2 as cv
import numpy as np

img = np.zeros((200, 200), np.uint8)
img[20:120, 20:120] = 255

result = cv.bitwise_not(img)

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
