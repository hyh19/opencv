import cv2 as cv

back = cv.imread('../images/back.jpeg')
cat = cv.imread('../images/small_cat_1.jpeg')

# 只有两张图的属性是一样的才可以进行溶合
print(back.shape)
print(cat.shape)

result = cv.addWeighted(cat, 0.7, back, 0.3, 0)
cv.imshow('result', result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()
