import cv2 as cv
import numpy as np

bgr_img = np.random.randint(0, 256, size=(2, 3, 3), dtype=np.uint8)
bgra_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2BGRA)
print(f'bgr = \n{bgr_img}')
print(f'bgra = \n{bgra_img}')

blue_img, green_img, red_img, alpha_img = cv.split(bgra_img)
print(f'alpha = \n{alpha_img}')

alpha_img[:, :] = 125
bgra_img = cv.merge([blue_img, green_img, red_img, alpha_img])
print(f'bgra = \n{bgra_img}')
