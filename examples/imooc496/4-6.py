import numpy as np
import cv2

img = np.zeros((480, 640, 3), np.uint8)

roi = img[100:400, 100:600]
# roi[:,:] = [0,0,255]
roi[:] = [0, 0, 255]
roi[:, 50] = [0, 0, 0]
roi[10:200, 10:200] = [0, 255, 0]

cv2.imshow('img', roi)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
