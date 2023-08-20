# -*- coding: utf-8 -*-
import cv2 as cv

red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)

img = cv.imread('cs.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, green, 2)

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
    cv.putText(img, text, pt, cv.FONT_HERSHEY_SIMPLEX, 1, red, 2)
    cv.circle(img, pt, 3, blue, -1)

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/NZZnLl
