import cv2 as cv

cv.namedWindow('new', cv.WINDOW_NORMAL)
cv.resizeWindow('new', 640, 480)
cv.imshow('new', 0)
key = cv.waitKey(0)
# 错误写法 3-4.py 修复
if key == 'q':
    exit()
cv.destroyAllWindows()
