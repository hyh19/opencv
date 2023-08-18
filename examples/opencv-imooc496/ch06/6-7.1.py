import cv2 as cv

# 导入图片
dog = cv.imread('../images/dog.jpeg')
dog[20:120, 20:120] = [0, 0, 255]
dog[80:180, 80:180] = [0, 255, 0]

cv.imshow('dog', dog)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
