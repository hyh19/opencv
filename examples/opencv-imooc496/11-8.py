import cv2

# 读文件
img1 = cv2.imread('images/opencv_search.png')
img2 = cv2.imread('images/opencv_orig.png')

# 灰度化
g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建 SIFT 对象
sift = cv2.xfeatures2d.SIFT_create()

# 使用 SIFT 进行检测
kp1, des1 = sift.detectAndCompute(g1, None)
kp2, des2 = sift.detectAndCompute(g2, None)

bf = cv2.BFMatcher(cv2.NORM_L1)
match = bf.match(des1, des2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow('img3', img3)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
