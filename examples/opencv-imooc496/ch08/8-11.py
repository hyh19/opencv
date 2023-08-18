import cv2 as cv

img = cv.imread('../images/lena.png')
result = cv.Canny(img, threshold1=100, threshold2=200)
cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# Canny: https://t.ly/AAXS
