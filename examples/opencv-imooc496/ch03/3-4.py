import cv2 as cv

cv.namedWindow('img', cv.WINDOW_NORMAL)
img = cv.imread('../images/hello.jpeg')
cv.imshow('img', img)
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
