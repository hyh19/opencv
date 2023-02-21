import cv2

cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 640, 360)

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 从摄像头读取视频帧
    ret, frame = cap.read()
    # 将视频帧在窗口中显示
    cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# 释放 VideoCapture
cap.release()
cv2.destroyAllWindows()
