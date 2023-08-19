import cv2 as cv

img = cv.imread('../images/dotinj.png')

kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
result = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

cv.imshow('img', img)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# morphologyEx: https://t.ly/6hb9x
