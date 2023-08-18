import cv2


def callback(x):
    pass


cv2.namedWindow('color', cv2.WINDOW_NORMAL)
img = cv2.imread('images/RMB.jpeg')
color_spaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
                cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV,
                cv2.COLOR_BGR2YUV]
cv2.createTrackbar('color_spaces', 'color', 0, len(color_spaces) - 1, callback)

while True:
    index = cv2.getTrackbarPos('color_spaces', 'color')
    # 颜色空间转换 API
    cvt_img = cv2.cvtColor(img, color_spaces[index])
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    print(key)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# https://bit.ly/3ENkINF
