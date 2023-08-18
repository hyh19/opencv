import cv2 as cv

cv.namedWindow('video', cv.WINDOW_NORMAL)
cv.resizeWindow('video', 640, 360)

cap = cv.VideoCapture(0)

while True:
    # 从摄像头读取视频帧
    ret, frame = cap.read()
    # 将视频帧在窗口中显示
    cv.imshow('video', frame)
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# 释放 VideoCapture
cap.release()
cv.destroyAllWindows()
