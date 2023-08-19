import cv2 as cv

img = cv.imread('../images/contours1.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_bin = cv.threshold(img_gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)
# img_bin = cv.adaptiveThreshold(img_gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                 thresholdType=cv.THRESH_BINARY, blockSize=11, C=0)

# 查找轮廓
contours, hierarchy = cv.findContours(img_bin, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv.drawContours(img, contours, contourIdx=-1, color=(0, 0, 255), thickness=1)

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# findContours: https://t.ly/9M2x
# drawContours: https://t.ly/d0KO
