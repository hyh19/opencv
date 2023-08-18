import cv2 as cv

img = cv.imread('../images/math.png')
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

dst = cv.adaptiveThreshold(img1, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 0)
print(dst.shape)

cv.imshow('img', img)
cv.imshow('gray', img1)
cv.imshow('bin', dst)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# adaptiveThreshold: https://t.ly/j29S
