import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('../images/hello.jpeg')
cv2.imshow('img', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
