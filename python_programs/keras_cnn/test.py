# -*- coding: utf-8 -*-  
'''Trains a simple deep NN on the MNIST dataset.
Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.


https://blog.csdn.net/houchaoqun_xmu/article/details/78492718

zb:
erroProcess
/srv/anaconda3/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py

Modify:
return tf.nn.softmax(x, axis=axis)  ------>  return tf.nn.softmax(x, dim=axis)
'''
 
from __future__ import print_function
 
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
 
batch_size = 128
num_classes = 10
epochs = 2
 
# the data, shuffled and split between train and test sets 
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
 
import numpy as np
path='/root/Downloads/mnist.npz'
f = np.load(path)
x_train, y_train = f['x_train'], f['y_train']
x_test, y_test = f['x_test'], f['y_test']
f.close()
print("Load Dataset OK")

x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
 
# convert class vectors to binary class matrices
# label为0~9共10个类别，keras要求格式为binary class matrices
 
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
 
# add by hcq-20171106
# Dense of keras is full-connection.
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))
 
model.summary()
 
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])
 
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])



