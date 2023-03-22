# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('cs.bmp')

# --------获取并绘制轮廓-----------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, np.uint8)
cnt = contours[0]
cv.drawContours(mask, [cnt], 0, 255, -1)

# --------计算极值-----------------
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

# --------计算极值-----------------
print("leftmost=", leftmost)
print("rightmost=", rightmost)
print("topmost=", topmost)
print("bottommost=", bottommost)

# --------绘制说明文字-----------------
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(o, 'A', leftmost, font, 1, (0, 0, 255), 2)
cv.circle(o, leftmost, 3, [255, 0, 0], -1)
cv.putText(o, 'B', rightmost, font, 1, (0, 0, 255), 2)
cv.circle(o, rightmost, 3, [255, 0, 0], -1)
cv.putText(o, 'C', topmost, font, 1, (0, 0, 255), 2)
cv.circle(o, topmost, 3, [255, 0, 0], -1)
cv.putText(o, 'D', bottommost, font, 1, (0, 0, 255), 2)
cv.circle(o, bottommost, 3, [255, 0, 0], -1)

# --------绘制图像-----------------
cv.imshow("result", o)

# --------释放窗口-----------------
cv.waitKey()
cv.destroyAllWindows()
