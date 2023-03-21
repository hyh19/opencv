# -*- coding: utf-8 -*-
import cv2

o = cv2.imread('cc.bmp')
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(binary,
                                              cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)
area, trgl = cv2.minEnclosingTriangle(contours[0])
print("area=", area)
print("trgl:", trgl)
for i in range(0, 3):
    cv2.line(o, tuple(trgl[i][0].astype(int)),
             tuple(trgl[(i + 1) % 3][0].astype(int)), (0, 0, 255), 2)
cv2.imshow("result", o)
cv2.waitKey()
cv2.destroyAllWindows()

# numpy.ndarray.astype: https://bit.ly/3Tyhmof
