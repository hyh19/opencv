import cv2

# 读文件
img = cv2.imread('chess.png')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建 ORB 对象
orb = cv2.ORB_create()

# 使用 ORB 进行检测
kp, des = orb.detectAndCompute(gray, None)

# 绘制 keypoints
cv2.drawKeypoints(gray, kp, img)

cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
