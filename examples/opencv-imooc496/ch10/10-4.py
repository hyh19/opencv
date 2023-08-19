import cv2 as cv

img = cv.imread('../images/contours1.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_bin = cv.threshold(img_gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv.findContours(img_bin, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv.drawContours(img, contours, contourIdx=-1, color=(0, 0, 255), thickness=1)

# 计算面积
area = cv.contourArea(contours[0])
print(f'area = {area}')

# 计算周长
length = cv.arcLength(contours[0], closed=True)
print(f'len = {length}')

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# contourArea: https://t.ly/Lo80T
