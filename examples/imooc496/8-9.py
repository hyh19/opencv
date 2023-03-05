import cv2

img = cv2.imread('chess.png')

# 沙尔算子 y 方向边缘
d1 = cv2.Scharr(img, cv2.CV_64F, 1, 0)

# 沙尔算子 x 方向边缘
d2 = cv2.Scharr(img, cv2.CV_64F, 0, 1)

dst = cv2.add(d1, d2)

cv2.imshow('img', img)
cv2.imshow('d1', d1)
cv2.imshow('d2', d2)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# Scharr: https://t.ly/Rtef
