import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('/Users/hyh/Downloads/input.jpg')
cv2.imshow('img', img)
key = cv2.waitKey(0)
# TODO 3-4.py 修复
if key == 'q':
    exit()
cv2.destroyAllWindows()
