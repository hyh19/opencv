import cv2 as cv

cv.namedWindow('img', cv.WINDOW_NORMAL)
img = cv.imread('../images/hello.jpeg')
cv.imshow('img', img)
key = cv.waitKey(0)
# 错误写法 3-4.py 修复
if key == 'q':
    exit()
cv.destroyAllWindows()
