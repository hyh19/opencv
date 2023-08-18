import cv2 as cv

cv.namedWindow('video', cv.WINDOW_NORMAL)
cv.resizeWindow('video', 640, 360)

# 打开视频文件
cap = cv.VideoCapture('../images/video.mp4')

while True:
    # 从视频文件读取视频帧
    ret, frame = cap.read()
    # 将视频帧在窗口中显示
    cv.imshow('video', frame)
    # fps = 30
    key = cv.waitKey(33)
    if key & 0xFF == ord('q'):
        break

# 释放 VideoCapture
cap.release()
cv.destroyAllWindows()
