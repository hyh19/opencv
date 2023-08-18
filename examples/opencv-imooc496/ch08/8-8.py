import cv2 as cv

img = cv.imread('../images/chess.png')
dx = cv.Sobel(img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
dy = cv.Sobel(img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
result = cv.add(dx, dy)

cv.imshow('img', img)
cv.imshow('dx', dx)
cv.imshow('dy', dy)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# Sobel: https://bit.ly/3JRSzIs
