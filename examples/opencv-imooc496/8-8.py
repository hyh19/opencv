import cv2

img = cv2.imread('images/chess.png')
d1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
d2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
dst = cv2.add(d1, d2)

cv2.imshow('img', img)
cv2.imshow('d1', d1)
cv2.imshow('d2', d2)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# Sobel: https://bit.ly/3JRSzIs
