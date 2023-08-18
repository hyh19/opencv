import cv2

img = cv2.imread('../images/dog.jpeg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)
print(dst.shape)

cv2.imshow('img', img)
cv2.imshow('gray', img1)
cv2.imshow('bin', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# threshold: https://t.ly/BVBu
