import cv2 as cv

img = cv.imread('../images/dog.jpeg')
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, dst = cv.threshold(img1, 180, 255, cv.THRESH_BINARY)
print(dst.shape)

cv.imshow('img', img)
cv.imshow('gray', img1)
cv.imshow('bin', dst)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# threshold: https://t.ly/BVBu
