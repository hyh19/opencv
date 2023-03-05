import cv2

img = cv2.imread('lena.png')

dst = cv2.Canny(img, 100, 200)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# Canny: https://t.ly/AAXS
