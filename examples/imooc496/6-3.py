import cv2

back = cv2.imread('./back.jpeg')
small_cat = cv2.imread('./small_cat_1.jpeg')

# 只有两张图的属性是一样的才可以进行溶合
print(back.shape)
print(small_cat.shape)

result = cv2.addWeighted(small_cat, 0.7, back, 0.3, 0)
cv2.imshow('result', result)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
