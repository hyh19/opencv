import cv2 as cv

cv.namedWindow('video', cv.WINDOW_NORMAL)
cv.resizeWindow('video', 640, 360)

# 打开摄像头
cap = cv.VideoCapture(0)

# 创建 VideoWriter 写视频文件
fourcc = cv.VideoWriter_fourcc(*'MJPG')
vw = cv.VideoWriter('/Users/hyh/Downloads/output.mp4', fourcc, 25, (1280, 720))

# 判断摄像头是否为打开关态
while cap.isOpened():
    # 从摄像头读取视频帧
    ret, frame = cap.read()
    if ret is True:
        # 将视频帧在窗口中显示
        cv.imshow('video', frame)
        # 重新将窗口设定为指定大小
        cv.resizeWindow('video', 640, 360)
        # 写数据到视频文件
        vw.write(frame)
        key = cv.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    else:
        break

# 释放 VideoCapture
cap.release()
# 释放 VideoWriter
vw.release()
cv.destroyAllWindows()
