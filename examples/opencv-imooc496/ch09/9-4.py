import cv2 as cv

img = cv.imread('../images/math.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_bin = cv.adaptiveThreshold(img_gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               thresholdType=cv.THRESH_BINARY, blockSize=11, C=0)

cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('img_bin', img_bin)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# adaptiveThreshold: https://t.ly/j29S
