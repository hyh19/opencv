import cv2

img = cv2.imread('papper.png')

# 中值滤波
dst = cv2.medianBlur(img, 5)

cv2.imshow('dst', dst)
cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# medianBlur: t.ly/mI_R
