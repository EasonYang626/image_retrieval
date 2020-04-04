import keras
import time

from keras.engine.saving import load_model
from keras_applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.optimizers import SGD
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt
import tensorflow as tf
from numpy import linalg as LA
from keras.preprocessing import image
import numpy as np

NUM_CLASSES = 80
TRAIN_PATH = 'data/train'
TEST_PATH = 'data/val'

PREDICT_IMG = 'database1/29010.jpg'
# FC层定义输入层的大小
FC_NUMS = 1024
# 冻结训练的层数，根据模型的不同，层数也不一样，根据调试的结果，VGG19和VGG16c层比较符合理想的测试结果
FREEZE_LAYERS = 17
# 进行训练和测试的图片大小，VGG19推荐为224×244
IMAGE_SIZE = 224
BATCH_SIZE = 16


class LossHistory(keras.callbacks.Callback):
    # 函数开始时创建盛放loss与acc的容器
    def on_train_begin(self, logs={}):
        self.losses = {'batch': [], 'epoch': []}
        self.accuracy = {'batch': [], 'epoch': []}
        self.val_loss = {'batch': [], 'epoch': []}
        self.val_acc = {'batch': [], 'epoch': []}

    # 按照batch来进行追加数据
    def on_batch_end(self, batch, logs={}):
        # 每一个batch完成后向容器里面追加loss，acc
        self.losses['batch'].append(logs.get('loss'))
        self.accuracy['batch'].append(logs.get('acc'))
        self.val_loss['batch'].append(logs.get('val_loss'))
        self.val_acc['batch'].append(logs.get('val_acc'))
        # 每五秒按照当前容器里的值来绘图
        if int(time.time()) % 5 == 0:
            self.draw_p(self.losses['batch'], 'loss', 'train_batch')
            self.draw_p(self.accuracy['batch'], 'acc', 'train_batch')
            self.draw_p(self.val_loss['batch'], 'loss', 'val_batch')
            self.draw_p(self.val_acc['batch'], 'acc', 'val_batch')

    def on_epoch_end(self, batch, logs={}):
        # 每一个epoch完成后向容器里面追加loss，acc
        self.losses['epoch'].append(logs.get('loss'))
        self.accuracy['epoch'].append(logs.get('acc'))
        self.val_loss['epoch'].append(logs.get('val_loss'))
        self.val_acc['epoch'].append(logs.get('val_acc'))
        # 每五秒按照当前容器里的值来绘图
        if int(time.time()) % 5 == 0:
            self.draw_p(self.losses['epoch'], 'loss', 'train_epoch')
            self.draw_p(self.accuracy['epoch'], 'acc', 'train_epoch')
            self.draw_p(self.val_loss['epoch'], 'loss', 'val_epoch')
            self.draw_p(self.val_acc['epoch'], 'acc', 'val_epoch')

    # 绘图，这里把每一种曲线都单独绘图，若想把各种曲线绘制在一张图上的话可修改此方法
    def draw_p(self, lists, label, type):
        plt.figure()
        plt.plot(range(len(lists)), lists, 'r', label=label)
        plt.ylabel(label)
        plt.xlabel(type)
        plt.legend(loc="upper right")
        plt.savefig(type + '_' + label + '.jpg')

    # 由于这里的绘图设置的是5s绘制一次，当训练结束后得到的图可能不是一个完整的训练过程（最后一次绘图结束，有训练了0-5秒的时间）
    # 所以这里的方法会在整个训练结束以后调用
    def end_draw(self):
        self.draw_p(self.losses['batch'], 'loss', 'train_batch')
        self.draw_p(self.accuracy['batch'], 'acc', 'train_batch')
        self.draw_p(self.val_loss['batch'], 'loss', 'val_batch')
        self.draw_p(self.val_acc['batch'], 'acc', 'val_batch')
        self.draw_p(self.losses['epoch'], 'loss', 'train_epoch')
        self.draw_p(self.accuracy['epoch'], 'acc', 'train_epoch')
        self.draw_p(self.val_loss['epoch'], 'loss', 'val_epoch')
        self.draw_p(self.val_acc['epoch'], 'acc', 'val_epoch')



class VGG:
    def build(self):
        base_model = VGG19(input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3), include_top=False, weights='imagenet')
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(FC_NUMS, activation='relu')(x)
        prediction = Dense(NUM_CLASSES, activation='softmax')(x)
        self.model = Model(inputs=base_model.input, outputs=prediction)
        self.model.summary()
        print("layer nums:", len(self.model.layers))
        for layer in self.model.layers[:FREEZE_LAYERS]:
            layer.trainable = False
        for layer in self.model.layers[FREEZE_LAYERS:]:
            layer.trainable = True
        for layer in self.model.layers:
            print("layer.trainable:", layer.trainable)

        self.model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy',
                           metrics=['accuracy'])

        # 给出训练图片的生成器， 其中classes定义后，可让model按照这个顺序进行识别
        self.train_datagen = ImageDataGenerator()
        self.train_generator = self.train_datagen.flow_from_directory(directory=TRAIN_PATH,
                                                                      target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                                      batch_size=BATCH_SIZE)
        self.test_datagen = ImageDataGenerator()
        self.test_generator = self.test_datagen.flow_from_directory(directory=TEST_PATH,
                                                                    target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                                    batch_size=BATCH_SIZE)
    def __init__(self):

        self.model = load_model('new_model.h5')
        self.model.predict(np.zeros((1, 224, 224, 3)))
        print(self.extract_feat(PREDICT_IMG))

    def train_model(self):
        # 运行模型
        logs_loss = LossHistory()
        self.model.fit_generator(self.train_generator, epochs=10, validation_data=self.test_generator, callbacks=[logs_loss])
        self.model.save('new_model.h5')
        # 找一张图片进行预测验证
        img = load_img(path=PREDICT_IMG, target_size=(IMAGE_SIZE, IMAGE_SIZE))
        # 转换成numpy数组
        x = img_to_array(img)
        # 转换后的数组为3维数组(224,224,3),
        # 而训练的数组为4维(图片数量, 224,224, 3),所以我们可扩充下维度
        x = K.expand_dims(x, axis=0)
        # 需要被预处理下
        x = preprocess_input(x)
        # 数据预测
        result = self.model.predict(x, steps=1)
        print("result:", K.eval(K.argmax(result)))
        logs_loss.end_draw()


    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        mean = np.mean(feat[0])
        i = 0
        while i< len(feat[0]):
            feat[0][i] = feat[0][i] - mean
            i = i+1
        a = np.std(feat[0],ddof=0)
        # norm_feat = feat[0]/ LA.norm(feat[0])
        norm_feat = feat[0] / a
        return norm_feat

if __name__ == '__main__':
    vgg = VGG()
    vgg.build()
    vgg.train_model()
