import cv2
from cv2 import dnn
import numpy as np

# 配置文件、模型文件和分类标签文件路径
config_path = 'model/bvlc_googlenet.prototxt'
model_path = 'model/bvlc_googlenet.caffemodel'
class_path = 'model/synset_words.txt'

# 加载神经网络和分类标签
network = dnn.readNetFromCaffe(config_path, model_path)
with open(class_path, 'rt') as f:
    class_names = [line[line.find(" ") + 1:].strip() for line in f]

# 图像预处理和前向传递
image = cv2.imread('smallcat.jpeg')
blob = dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
network.setInput(blob)
predictions = network.forward()

# 输出前 N 个高概率预测
top_n = 3
indexes = np.argsort(predictions[0])[::-1][:top_n]
scores = predictions[0][indexes]

for i in range(top_n):
    class_index = indexes[i]
    class_name = class_names[class_index]
    print('Top {} [class: {}], [line: {}], [score: {}]'.format(i + 1, class_name, class_index + 1, scores[i]))
