import cv2 as cv
import pytesseract

img = cv.imread('chinacar.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

classifier = cv.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')
plates = classifier.detectMultiScale(img_gray, 1.1, 3)
result = ''
for x, y, w, h in plates:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    img_gray_roi = img_gray[y:y + h, x:x + w]
    _, img_gray_roi_bin = cv.threshold(img_gray_roi, 0, 255, cv.THRESH_OTSU)
    result = pytesseract.image_to_string(img_gray_roi_bin, lang='chi_sim+eng', config='--psm 8 --oem 3')

cv.imshow(f'Result: {result}', img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/ZDvZ01
