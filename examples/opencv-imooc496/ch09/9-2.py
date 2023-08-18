import cv2 as cv

img = cv.imread('../images/dog.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh, img_bin = cv.threshold(img_gray, thresh=180, maxval=255, type=cv.THRESH_BINARY)

cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('img_bin', img_bin)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# threshold: https://t.ly/BVBu
