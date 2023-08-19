import cv2 as cv
from cv2 import dnn
import numpy as np

# 配置文件、模型文件和分类标签文件路径
prototxt = 'model/bvlc_googlenet.prototxt'
caffe_model = 'model/bvlc_googlenet.caffemodel'
class_path = 'model/synset_words.txt'

# 加载神经网络和分类标签
network = dnn.readNetFromCaffe(prototxt, caffe_model)
with open(class_path, 'rt') as f:
    class_names = [line[line.find(' ') + 1:].strip() for line in f]

# 图像预处理和前向传递
image = cv.imread('smallcat.jpeg')
blob = dnn.blobFromImage(image, scalefactor=1, size=(224, 224), mean=(104, 117, 123))
network.setInput(blob)
predictions = network.forward()

# 输出前 N 个高概率预测
top_n = 3
indexes = np.argsort(predictions[0])[::-1][:top_n]
scores = predictions[0][indexes]

for i in range(top_n):
    class_index = indexes[i]
    class_name = class_names[class_index]
    print(f'Top {i + 1} [class: {class_name}], [line: {class_index + 1}], [score: {scores[i]}]')

'''
运行结果：

Top 1 [class: tabby, tabby cat], [line: 282], [score: 0.2257317304611206]
Top 2 [class: Egyptian cat], [line: 286], [score: 0.1566489040851593]
Top 3 [class: Persian cat], [line: 284], [score: 0.1038256511092186]
'''
