import cv2 as cv

img = cv.imread('../images/j.png')

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
print(kernel)

dst = cv.dilate(img, kernel, iterations=1)

cv.imshow('img', img)
cv.imshow('dst', dst)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# dilate: https://t.ly/Mkxq
