import cv2 as cv

cv.namedWindow('img', cv.WINDOW_NORMAL)
img = cv.imread('../images/hello.jpeg')
while True:
    cv.imshow('img', img)
    key = cv.waitKey(0)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'):
        cv.imwrite('/Users/hyh/Downloads/output.png', img)
    else:
        print(key)
cv.destroyAllWindows()
