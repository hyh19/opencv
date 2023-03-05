import cv2

# harris
blockSize = 2
ksize = 3
k = 0.04

img = cv2.imread('chess.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris 角点检测
dst = cv2.cornerHarris(gray, blockSize, ksize, k)

# Harris 角点的展示
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('harris', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# cornerHarris: https://t.ly/g1TL
