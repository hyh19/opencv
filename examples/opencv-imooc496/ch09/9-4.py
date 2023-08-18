import cv2

img = cv2.imread('../images/math.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 0)
print(dst.shape)

cv2.imshow('img', img)
cv2.imshow('gray', img1)
cv2.imshow('bin', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# adaptiveThreshold: https://t.ly/j29S
