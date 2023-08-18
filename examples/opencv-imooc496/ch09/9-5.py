import cv2
import numpy as np

img = cv2.imread('../images/j.png')

kernel = np.ones((3, 3), np.uint8)
dst = cv2.erode(img, kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# erode: https://t.ly/3GTc
