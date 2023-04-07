import cv2 as cv
import numpy as np

bgr_img = cv.imread('lenacolor.png')
cv.imshow('bgr', bgr_img)

bgra_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2BGRA)
blue_img, green_img, red_img, alpha_img = cv.split(bgra_img)
alpha_list = [255, 125, 0]
for alpha in alpha_list:
    alpha_img[:, :] = alpha
    bgra_img = cv.merge([blue_img, green_img, red_img, alpha_img])
    cv.imshow(f'bgr_alpha_{alpha}', bgra_img)
    cv.imwrite(f'bgr_alpha_{alpha}.png', bgra_img)

cv.waitKey()
cv.destroyAllWindows()
