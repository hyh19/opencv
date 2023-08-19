import cv2 as cv

img = cv.imread('p3.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

classifier = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

faces = classifier.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3)

for x, y, w, h in faces:
    cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)

cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/wK6glU
