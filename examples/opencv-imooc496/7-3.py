import cv2

dog = cv2.imread('images/dog.jpeg')
new1 = cv2.rotate(dog, cv2.ROTATE_90_CLOCKWISE)
new2 = cv2.rotate(dog, cv2.ROTATE_180)

cv2.imshow('dog', dog)
cv2.imshow('new1', new1)
cv2.imshow('new2', new2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# rotate: https://t.ly/Z74e
