import cv2 as cv

bgr_img = cv.imread('lesson2.jpg')
hsv_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)
hue_img, sat_img, val_img = cv.split(hsv_img)

hue_mask = cv.inRange(hue_img, 5, 170)
sat_mask = cv.inRange(sat_img, 25, 166)
mask = hue_mask & sat_mask
roi_img = cv.bitwise_and(bgr_img, bgr_img, mask=mask)

cv.imshow('bgr', bgr_img)
cv.imshow('roi', roi_img)
cv.waitKey()
cv.destroyAllWindows()
