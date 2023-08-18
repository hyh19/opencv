import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('../images/hello.jpeg')
cv2.imshow('img', img)
key = cv2.waitKey(0)
# 错误写法 3-4.py 修复
if key == 'q':
    exit()
cv2.destroyAllWindows()
