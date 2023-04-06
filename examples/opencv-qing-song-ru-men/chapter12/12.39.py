# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/NZZnLl

img = cv.imread('cs.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
# x 坐标最小的点
left_most = tuple(cnt[cnt[:, :, 0].argmin()][0])
# x 坐标最大的点
right_most = tuple(cnt[cnt[:, :, 0].argmax()][0])
# y 坐标最小的点
top_most = tuple(cnt[cnt[:, :, 1].argmin()][0])
# y 坐标最大的点
bottom_most = tuple(cnt[cnt[:, :, 1].argmax()][0])

print(f'leftmost = {left_most}')
print(f'rightmost = {right_most}')
print(f'topmost = {top_most}')
print(f'bottommost = {bottom_most}')

texts = ['A', 'B', 'C', 'D']
pts = [left_most, right_most, top_most, bottom_most]
for text, pt in zip(texts, pts):
    cv.putText(img, text, pt, cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv.circle(img, pt, 3, [255, 0, 0], -1)
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
