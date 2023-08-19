import cv2 as cv

# 读文件
img = cv.imread('../images/contours1.jpeg')

print(img.shape)

# 转变成单通道
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv.drawContours(img, contours, -1, (0, 0, 255), 1)

# 计算面积
area = cv.contourArea(contours[0])
print("area=%d" % area)

# 计算周长
length = cv.arcLength(contours[0], False)
print("len=%d" % length)

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# contourArea: https://t.ly/Lo80T
