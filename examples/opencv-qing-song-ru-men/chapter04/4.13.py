# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3ZwRATe

img = cv.imread("lenacolor.png")
bgra = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
b, g, r, a = cv.split(bgra)
a[:, :] = 125
bgra125 = cv.merge([b, g, r, a])
a[:, :] = 0
bgra0 = cv.merge([b, g, r, a])
cv.imshow("img", img)
cv.imshow("bgra", bgra)
cv.imshow("bgra125", bgra125)
cv.imshow("bgra0", bgra0)
cv.waitKey()
cv.destroyAllWindows()
# cv.imwrite("bgra.png", bgra)
# cv.imwrite("bgra125.png", bgra125)
# cv.imwrite("bgra0.png", bgra0)
