import cv2 as cv

img = cv.imread('../images/RMB.jpeg')

# 浅拷贝
img_shallow_copy = img

# 深拷贝
img_deep_copy = img.copy()

img[10:100, 10:100] = [0, 255, 0]

cv.imshow('img', img)
cv.imshow('img_shallow_copy', img_shallow_copy)
cv.imshow('img_deep_copy', img_deep_copy)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
