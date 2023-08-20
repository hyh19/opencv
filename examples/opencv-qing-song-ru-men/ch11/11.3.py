# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("lena.bmp")
down = cv.pyrDown(o)
up = cv.pyrUp(down)
diff = up - o  # 构造diff图像，查看up与o的区别
print("o.shape=", o.shape)
print("up.shape=", up.shape)
cv.imshow("original", o)
cv.imshow("up", up)
cv.imshow("difference", diff)
cv.waitKey()
cv.destroyAllWindows()
