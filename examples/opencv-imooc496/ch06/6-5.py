import cv2 as cv
import numpy as np

img1 = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)

img1[20:120, 20:120] = 255
img2[80:180, 80:180] = 255

result = cv.bitwise_and(img1, img2)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
