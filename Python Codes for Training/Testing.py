    ### GPUs allocations + Libraries importing###
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID";
# The GPU id to use, usually either "0" or "1";
os.environ["CUDA_VISIBLE_DEVICES"] = "3";
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.compat.v1.keras.backend import set_session
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
config.log_device_placement = True  # to log device placement (on which device the operation ran)
sess = tf.compat.v1.Session(config=config)
set_session(sess)
from tensorflow.keras import optimizers
import tensorflow.keras as keras
import tensorflow.keras.backend as K


 ### Import Datasets ###
from tensorflow.keras.preprocessing.image import ImageDataGenerator
seed=2020
Data_datagen=ImageDataGenerator() #included in our dependencies
Data_datagen1=ImageDataGenerator() #included in our dependencies
import numpy as np
target_size=(288,432)
batch_size=1



Test=Data_datagen1.flow_from_directory('Data/Test',
                                                     target_size=target_size,
                                                     color_mode='grayscale',
                                                     batch_size=batch_size,
                                                   shuffle=True,seed=seed)
  ## Load MOdels and Weights ###
from Model import Model2
model= Model2()  
model.summary()
model.load_weights("low2.h5")

   ### INFERENCE ###
Adam = optimizers.Adam(lr=0.0,  beta_1=0.9, beta_2=0.99)
model.compile(optimizer=Adam, loss="categorical_crossentropy",metrics=['accuracy'])
model.evaluate_generator(Test,300)  ## Quanitative Analysis









