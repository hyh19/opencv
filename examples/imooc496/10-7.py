import cv2

min_w = 90
min_h = 90

# 检测线的高度
line_high = 550

# 线的偏移
offset = 7

# 统计车的数量
car_num = 0

# 存放有效车辆的数组
cars = []


def getCenter(px, py, width, height):
    cx = px + width // 2
    cy = py + height // 2
    return cx, cy


cap = cv2.VideoCapture('/Users/hyh/Downloads/video.mp4')

bg_sub_mog = cv2.bgsegm.createBackgroundSubtractorMOG()

# 形态学 kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while True:
    ret, frame = cap.read()
    if ret:
        # 灰度
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 去噪（高斯）
        blur = cv2.GaussianBlur(frame, (3, 3), 5)

        # 去背影
        mask = bg_sub_mog.apply(blur)

        # 腐蚀，去掉图中小斑块
        erode = cv2.erode(mask, kernel)

        # 膨胀，还原放大
        dilate = cv2.dilate(erode, kernel, iterations=3)

        # 闭运算，去掉物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

        contours, hierarchy = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 画一条检测线
        cv2.line(frame, (10, line_high), (1200, line_high), (255, 255, 0), 3)

        for c in contours:
            (x, y, w, h) = cv2.boundingRect(c)

            # 对车辆的宽高进行检测
            # 以验证是否是有效的车辆
            if w < min_w or h < min_h:
                continue

            # 到这里都是有效的车
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            center = getCenter(x, y, w, h)
            cars.append(center)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        for (x, y) in cars:
            if line_high - offset < y < line_high + offset:
                car_num += 1
                cars.remove((x, y))
                print(car_num)
        cv2.putText(frame, "Cars Count: " + str(car_num), (500, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
        cv2.imshow('video', frame)
        # cv2.imshow('erode', close)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# createBackgroundSubtractorMOG: https://t.ly/QnNf
