import cv2 as cv

img = cv.imread('../images/tophat.png')

kernel = cv.getStructuringElement(cv.MORPH_RECT, (19, 19))
print(kernel)

dst = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

cv.imshow('img', img)
cv.imshow('dst', dst)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# morphologyEx: https://t.ly/6hb9x
