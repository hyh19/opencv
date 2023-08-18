import cv2

img = cv2.imread('images/j.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(kernel)

dst = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# dilate: https://t.ly/Mkxq
