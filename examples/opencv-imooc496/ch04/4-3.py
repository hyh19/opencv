import cv2 as cv


def callback(x):
    pass


cv.namedWindow('color', cv.WINDOW_NORMAL)
img = cv.imread('../images/RMB.jpeg')
color_spaces = [cv.COLOR_BGR2RGBA, cv.COLOR_BGR2BGRA,
                cv.COLOR_BGR2GRAY, cv.COLOR_BGR2HSV,
                cv.COLOR_BGR2YUV]
cv.createTrackbar('color_spaces', 'color', 0, len(color_spaces) - 1, callback)

while True:
    index = cv.getTrackbarPos('color_spaces', 'color')
    # 颜色空间转换 API
    cvt_img = cv.cvtColor(img, color_spaces[index])
    cv.imshow('color', cvt_img)
    key = cv.waitKey(10)
    print(key)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

# https://bit.ly/3ENkINF
