import cv2 as cv


def draw_cruve(canvas, curve):
    i, n = 0, len(curve)
    while i < n:
        cv.line(canvas, pt1=curve[i % n][0], pt2=curve[(i + 1) % n][0],
                color=(0, 0, 255), thickness=1)
        i += 1


img = cv.imread('../images/hand.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_bin = cv.threshold(img_gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv.findContours(img_bin, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv.drawContours(img, contours, contourIdx=-1, color=(0, 0, 255), thickness=1)

approx_curve = cv.approxPolyDP(contours[0], epsilon=5, closed=True)
draw_cruve(img, approx_curve)

hull = cv.convexHull(contours[0])
draw_cruve(img, hull)

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# approxPolyDP: https://t.ly/Wsku
# convexHull: https://t.ly/6tCB
