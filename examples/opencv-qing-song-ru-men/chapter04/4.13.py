# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/uLHVYH

bgr = cv.imread("lenacolor.png")
cv.imshow("bgr", bgr)

bgr_alpha_255 = cv.cvtColor(bgr, cv.COLOR_BGR2BGRA)
blue, green, red, alpha = cv.split(bgr_alpha_255)
cv.imshow("bgr_alpha_255", bgr_alpha_255)
cv.imwrite("bgr_alpha_255.png", bgr_alpha_255)

alpha[:, :] = 125
bgr_alpha_125 = cv.merge([blue, green, red, alpha])
cv.imshow("bgr_alpha_125", bgr_alpha_125)
cv.imwrite("bgr_alpha_125.png", bgr_alpha_125)

alpha[:, :] = 0
bgr_alpha_0 = cv.merge([blue, green, red, alpha])
cv.imshow("bgr_alpha_0", bgr_alpha_0)
cv.imwrite("bgr_alpha_0.png", bgr_alpha_0)

cv.waitKey()
cv.destroyAllWindows()
