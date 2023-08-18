import cv2 as cv
import numpy as np

img1 = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)

img1[20:120, 20:120] = 255
img2[80:180, 80:180] = 255

result_or = cv.bitwise_or(img1, img2)
result_xor = cv.bitwise_xor(img1, img2)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('result_or', result_or)
cv.imshow('result_xor', result_xor)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
