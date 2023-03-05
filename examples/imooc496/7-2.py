import cv2

dog = cv2.imread('dog.jpeg')
new1 = cv2.flip(dog, 0)
new2 = cv2.flip(dog, 1)
new3 = cv2.flip(dog, -1)

cv2.imshow('dog', dog)
cv2.imshow('new1', new1)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# flip: https://bit.ly/3ydxTDX
