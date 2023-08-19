import cv2 as cv

img = cv.imread('../images/j.png')

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
result = cv.erode(img, kernel, iterations=1)

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# getStructuringElement: https://t.ly/FSUed