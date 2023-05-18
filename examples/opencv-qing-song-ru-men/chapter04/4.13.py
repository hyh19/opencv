# -*- coding: utf-8 -*-
import cv2 as cv

bgr_img = cv.imread('lenacolor.png')
cv.imshow('bgr', bgr_img)

bgra_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2BGRA)
for alpha in [255, 125, 0]:
    bgra_img[:, :, 3] = alpha
    cv.imshow(f'bgr_alpha_{alpha}', bgra_img)
    cv.imwrite(f'bgr_alpha_{alpha}.png', bgra_img)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/uLHVYH
