import cv2

dog = cv2.imread('./dog.jpeg')
print(dog.shape)
new = cv2.resize(dog, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
cv2.imshow('dog', dog)
cv2.imshow('new', new)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
