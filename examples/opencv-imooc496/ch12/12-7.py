import cv2 as cv
import numpy as np


class App:
    def __init__(self):
        self.img = None
        self.img_original = None
        self.mask = None
        self.output = None
        self.flag_rect = False
        self.rect = (0, 0, 0, 0)
        self.startX = 0
        self.startY = 0

    def on_mouse(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.flag_rect = True
            self.startX = x
            self.startY = y
        elif event == cv.EVENT_LBUTTONUP:
            self.flag_rect = False
            cv.rectangle(self.img,
                         (self.startX, self.startY),
                         (x, y),
                         (0, 0, 255),
                         3)
            self.rect = (min(self.startX, x), min(self.startY, y),
                         abs(self.startX - x),
                         abs(self.startY - y))
        elif event == cv.EVENT_MOUSEMOVE:
            if self.flag_rect:
                self.img = self.img_original.copy()
                cv.rectangle(self.img,
                             (self.startX, self.startY),
                             (x, y),
                             (255, 0, 0),
                             3)

    def run(self):
        cv.namedWindow('input')
        cv.setMouseCallback('input', self.on_mouse)

        self.img = cv.imread('lena.png')
        self.img_original = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
        self.output = np.zeros(self.img.shape, np.uint8)

        while True:
            cv.imshow('input', self.img)
            cv.imshow('output', self.output)
            k = cv.waitKey(100)
            if k == 27:
                break

            if k == ord('g'):
                bgd_model = np.zeros((1, 65), np.float64)
                fgd_model = np.zeros((1, 65), np.float64)
                cv.grabCut(self.img_original, self.mask, self.rect,
                           bgd_model, fgd_model,
                           1,
                           cv.GC_INIT_WITH_RECT)
            tmp_mask = np.where((self.mask == 1) | (self.mask == 3), 255, 0).astype('uint8')
            self.output = cv.bitwise_and(self.img_original, self.img_original, mask=tmp_mask)


App().run()
