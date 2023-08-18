import cv2


def drawShape(src, points):
    i, n = 0, len(points)
    while i < n:
        x, y = points[i % n][0]
        x1, y1 = points[(i + 1) % n][0]
        cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        i = i + 1


# 读文件
img = cv2.imread('images/hand.png')

print(img.shape)

# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, 0, (0, 255, 0), 1)

e = 5
approx = cv2.approxPolyDP(contours[0], e, True)

drawShape(img, approx)

hull = cv2.convexHull(contours[0])

drawShape(img, hull)

cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# approxPolyDP: https://t.ly/Wsku
# convexHull: https://t.ly/6tCB
