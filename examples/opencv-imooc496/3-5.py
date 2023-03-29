import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('/Users/hyh/Downloads/input.jpg')
while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'):
        cv2.imwrite('/Users/hyh/Downloads/output.png', img)
    else:
        print(key)
cv2.destroyAllWindows()
