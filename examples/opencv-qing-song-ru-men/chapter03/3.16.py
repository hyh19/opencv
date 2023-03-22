# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3IRLc21

# 读取原始载体图像
lena = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
# 读取原始载体图像的shape值
r, c = lena.shape
mask = np.zeros((r, c), dtype=np.uint8)
mask[220:400, 250:350] = 1
# 获取一个key,打码、解码所使用的密钥
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)

# ============获取打码脸============
# 使用密钥key加密原始图像lena
lenaXorKey = cv.bitwise_xor(lena, key)
# 获取加密图像的脸部信息encryptFace
encryptFace = cv.bitwise_and(lenaXorKey, mask * 255)
# 将图像lena内的脸部值设置为0，得到noFace1
noFace1 = cv.bitwise_and(lena, (1 - mask) * 255)
# 得到打码的lena图像
maskFace = encryptFace + noFace1

# ============将打码脸解码============
# 将脸部打码的lena与密钥key异或，得到脸部的原始信息
extractOriginal = cv.bitwise_xor(maskFace, key)
# 将解码的脸部信息extractOriginal提取出来得到extractFace
extractFace = cv.bitwise_and(extractOriginal, mask * 255)
# 从脸部打码的lena内提取没有脸部信息的lena图像，得到noFace2
noFace2 = cv.bitwise_and(maskFace, (1 - mask) * 255)
# 得到解码的lena图像
extractLena = noFace2 + extractFace

# ============显示图像============
cv.imshow("lena", lena)
cv.imshow("mask", mask * 255)
cv.imshow("1-mask", (1 - mask) * 255)
cv.imshow("key", key)
cv.imshow("lenaXorKey", lenaXorKey)
cv.imshow("encryptFace", encryptFace)
cv.imshow("noFace1", noFace1)
cv.imshow("maskFace", maskFace)
cv.imshow("extractOriginal", extractOriginal)
cv.imshow("extractFace", extractFace)
cv.imshow("noFace2", noFace2)
cv.imshow("extractLena", extractLena)

cv.waitKey()
cv.destroyAllWindows()
