import cv2 as cv


def drawShape(src, points):
    i, n = 0, len(points)
    while i < n:
        x, y = points[i % n][0]
        x1, y1 = points[(i + 1) % n][0]
        cv.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        i = i + 1


# 读文件
img = cv.imread('../images/hand.png')

print(img.shape)

# 转变成单通道
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv.drawContours(img, contours, 0, (0, 255, 0), 1)

e = 5
approx = cv.approxPolyDP(contours[0], e, True)

drawShape(img, approx)

hull = cv.convexHull(contours[0])

drawShape(img, hull)

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# approxPolyDP: https://t.ly/Wsku
# convexHull: https://t.ly/6tCB
