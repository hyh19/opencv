import cv2

cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 640, 360)

# 打开视频文件
cap = cv2.VideoCapture("/Users/hyh/Downloads/input.mp4")

while True:
    # 从视频文件读取视频帧
    ret, frame = cap.read()
    # 将视频帧在窗口中显示
    cv2.imshow("video", frame)
    # fps = 30
    key = cv2.waitKey(33)
    if key & 0xFF == ord('q'):
        break

# 释放 VideoCapture
cap.release()
cv2.destroyAllWindows()
