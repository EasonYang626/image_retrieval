import os
import numpy as np
from keras.models import Sequential
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.utils.np_utils import to_categorical
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
imgs = []
labels = []
img_shape =(150,150)
# image generator
files = os.listdir('database1')
# read 1000 files for the generator
for img_file in files[:1000]:
    img = imread('database1/' + img_file).astype('float32')
    img = imresize(img, img_shape)
    imgs.append(img)

imgs = np.array(imgs)
train_gen = ImageDataGenerator(
     # rescale = 1./255,
     featurewise_center=True,
     featurewise_std_normalization=True,
     rotation_range=20,
     width_shift_range=0.2,
     height_shift_range=0.2,
     horizontal_flip=True)
val_gen = ImageDataGenerator(
     # rescale = 1./255,
     featurewise_center=True,
     featurewise_std_normalization=True)

train_gen.fit(imgs)
val_gen.fit(imgs)

# 4500 training images
train_iter = train_gen.flow_from_directory('data/train',class_mode='binary',
                                            target_size=img_shape,   batch_size=16)
# 501 validation images
val_iter = val_gen.flow_from_directory('data/val', class_mode='binary',
                                        target_size=img_shape, batch_size=16)

'''
# image generator debug
for x_batch, y_batch in img_iter:
    print(x_batch.shape)
    print(y_batch.shape)
    plt.imshow(x_batch[0])
    plt.show()
'''

# define the navie model using sequential model
model = Sequential()
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.summary()
# define the optimzers
model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=1e-4),
        metrics=['acc'])
history = model.fit_generator(
        generator=train_iter,
        steps_per_epoch=282,
        epochs=100,
        validation_data=val_iter,
        validation_steps=32
        )
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1,101)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.legend()
plt.show()