import cv2

# 导入图片
dog = cv2.imread('./dog.jpeg')
dog[20:120, 20:120] = [0, 0, 255]
dog[80:180, 80:180] = [0, 255, 0]

cv2.imshow('dog', dog)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
