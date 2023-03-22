# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("lena.bmp")
up = cv.pyrUp(o)
down = cv.pyrDown(up)
diff = down - o  # 构造diff图像，查看down与o的区别
print("o.shape=", o.shape)
print("down.shape=", down.shape)
cv.imshow("original", o)
cv.imshow("down", down)
cv.imshow("difference", diff)
cv.waitKey()
cv.destroyAllWindows()
