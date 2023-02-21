import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('/Users/hyh/Downloads/IMG_0385.JPG')
cv2.imshow('img', img)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
