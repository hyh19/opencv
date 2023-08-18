import cv2
import numpy as np

# Shi-Tomasi
maxCorners = 1000
ql = 0.01
minDistance = 10

img = cv2.imread('images/chess.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners, ql, minDistance)
corners = np.int0(corners)

# Shi-Tomasi 绘制角点
for c in corners:
    x, y = c.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('harris', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# goodFeaturesToTrack: https://t.ly/w72-
