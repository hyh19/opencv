import cv2

img = cv2.imread('/Users/hyh/Downloads/IMG_8503.JPG')

# 浅拷贝
img2 = img

# 深拷贝
img3 = img.copy()

img[10:100, 10:100] = [0, 255, 0]

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
