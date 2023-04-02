import cv2 as cv
import pytesseract

img = cv.imread('chinacar.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

classifier = cv.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')
plates = classifier.detectMultiScale(gray, 1.1, 3)
for (x, y, w, h) in plates:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    gray_roi = gray[y:y + h, x:x + w]
    _, gray_roi_bin = cv.threshold(gray_roi, 0, 255, cv.THRESH_OTSU)
    text = pytesseract.image_to_string(gray_roi_bin, lang='chi_sim+eng', config='--psm 8 --oem 3')
    print(text)

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()
