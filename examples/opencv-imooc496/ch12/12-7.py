import cv2
import numpy as np


class App:
    flag_rect = False
    rect = (0, 0, 0, 0)
    startX = 0
    startY = 0

    def onmouse(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.flag_rect = True
            self.startX = x
            self.startY = y
            print("LBUTTIONDOWN")
        elif event == cv2.EVENT_LBUTTONUP:
            self.flag_rect = False
            cv2.rectangle(self.img,
                          (self.startX, self.startY),
                          (x, y),
                          (0, 0, 255),
                          3)
            self.rect = (min(self.startX, x), min(self.startY, y),
                         abs(self.startX - x),
                         abs(self.startY - y))

            print("LBUTTIONUP")
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_rect == True:
                self.img = self.img2.copy()
                cv2.rectangle(self.img,
                              (self.startX, self.startY),
                              (x, y),
                              (255, 0, 0),
                              3)
            print("MOUSEMOVE")

        print("onmouse")

    def run(self):
        print("run...")

        cv2.namedWindow('input')
        cv2.setMouseCallback('input', self.onmouse)

        self.img = cv2.imread('../lena.png')
        self.img2 = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
        self.output = np.zeros(self.img.shape, np.uint8)

        while (1):
            cv2.imshow('input', self.img)
            cv2.imshow('output', self.output)
            k = cv2.waitKey(100)
            if k == 27:
                break

            if k == ord('g'):
                bgdmodel = np.zeros((1, 65), np.float64)
                fgdmodel = np.zeros((1, 65), np.float64)
                cv2.grabCut(self.img2, self.mask, self.rect,
                            bgdmodel, fgdmodel,
                            1,
                            cv2.GC_INIT_WITH_RECT)
            mask2 = np.where((self.mask == 1) | (self.mask == 3), 255, 0).astype('uint8')
            self.output = cv2.bitwise_and(self.img2, self.img2, mask=mask2)


App().run()
