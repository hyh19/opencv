import cv2
import pytesseract

img_bgr = cv2.imread('chinacar.jpeg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

car_plate_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')
car_plate_result = car_plate_classifier.detectMultiScale(img_gray, 1.1, 3)
for (x, y, w, h) in car_plate_result:
    cv2.rectangle(img_bgr, (x, y), (x + w, y + h), (0, 0, 255), 2)
    img_gray_roi = img_gray[y:y + h, x:x + w]
    _, img_gray_roi_bin = cv2.threshold(img_gray_roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(img_gray_roi_bin, lang='chi_sim+eng', config='--psm 8 --oem 3')
    print(text)

cv2.imshow('img_bgr', img_bgr)
cv2.waitKey()
