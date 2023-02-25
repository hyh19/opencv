import cv2

img = cv2.imread('chess.png')

# 拉普拉斯
dst = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# Laplacian: t.ly/0dTE
