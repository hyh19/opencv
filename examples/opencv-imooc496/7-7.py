import cv2
import numpy as np

img = cv2.imread('images/perspective.jpeg')

src = np.float32([[100, 1100], [2100, 1100], [0, 4000], [2500, 3900]])
dst = np.float32([[0, 0], [2300, 0], [0, 3000], [2300, 3000]])
M = cv2.getPerspectiveTransform(src, dst)
new = cv2.warpPerspective(img, M, (2300, 3000))

cv2.imshow('img', img)
cv2.imshow('new', new)

cv2.waitKey(0)
cv2.destroyAllWindows()

# getPerspectiveTransform: https://t.ly/LOKc
# warpPerspective: https://t.ly/uj5Y
