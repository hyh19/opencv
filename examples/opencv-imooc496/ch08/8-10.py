import cv2 as cv

img = cv.imread('../images/chess.png')
result = cv.Laplacian(img, ddepth=cv.CV_64F, ksize=5)

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# Laplacian: https://t.ly/0dTE
