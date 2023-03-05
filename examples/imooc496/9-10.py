import cv2

img = cv2.imread('j.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(kernel)

dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# morphologyEx: https://t.ly/6hb9x
