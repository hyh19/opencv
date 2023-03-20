# -*- coding: utf-8 -*-
import cv2

o = cv2.imread("lena.bmp")
up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down - o  # 构造diff图像，查看down与o的区别
print("o.shape=", o.shape)
print("down.shape=", down.shape)
cv2.imshow("original", o)
cv2.imshow("down", down)
cv2.imshow("difference", diff)
cv2.waitKey()
cv2.destroyAllWindows()
