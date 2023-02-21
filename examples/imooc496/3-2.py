import cv2

cv2.namedWindow('win', cv2.WINDOW_NORMAL)
cv2.resizeWindow('win', 1920, 1080)
cv2.imshow('win', 0)

key = cv2.waitKey(0)
if key == 'q':
    cv2.destroyAllWindows()
