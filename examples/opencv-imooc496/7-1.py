import cv2

# TODO 复习 8.18

dog = cv2.imread('images/dog.jpeg')
new = cv2.resize(dog, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

cv2.imshow('dog', dog)
cv2.imshow('new', new)

cv2.waitKey(0)
cv2.destroyAllWindows()

# resize: https://bit.ly/3SSovPW
