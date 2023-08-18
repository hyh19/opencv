import cv2 as cv

img = cv.imread('../images/j.png')

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
print(kernel)

dst = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow('img', img)
cv.imshow('dst', dst)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# morphologyEx: https://t.ly/6hb9x
