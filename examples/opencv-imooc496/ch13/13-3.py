import cv2 as cv
import pytesseract

img = cv.imread('chinacar.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

classifier = cv.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

plates = classifier.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3)

for x, y, w, h in plates:
    cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
    img_roi = img_gray[y:y + h, x:x + w]
    _, img_bin = cv.threshold(img_roi, thresh=0, maxval=255, type=cv.THRESH_OTSU)
    result = pytesseract.image_to_string(img_bin, lang='chi_sim+eng', config='--psm 8 --oem 3')
    cv.imshow(f'Result: {result}', img)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/ZDvZ01
