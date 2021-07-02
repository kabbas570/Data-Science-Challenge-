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

     ### Import Dataset ###
from tensorflow.keras.preprocessing.image import ImageDataGenerator
seed=2020
Data_datagen=ImageDataGenerator() #included in our dependencies
Data_datagen1=ImageDataGenerator() #included in our dependencies
import numpy as np
target_size=(288,432)
batch_size=2
Train=Data_datagen1.flow_from_directory('Data/Train',
                                                     target_size=target_size,
                                                     color_mode='grayscale',
                                                     batch_size=batch_size,
                                                   shuffle=True,seed=seed)
Valid=Data_datagen1.flow_from_directory('Data/Valid',
                                                     target_size=target_size,
                                                     color_mode='grayscale',
                                                     batch_size=batch_size,
                                                   shuffle=True,seed=seed)
Test=Data_datagen1.flow_from_directory('Data/Test',
                                                     target_size=target_size,
                                                     color_mode='rgb',
                                                     batch_size=batch_size,
                                                   shuffle=True,seed=seed)

   ### Import the Model ###
from Model import Model3
model= Model3()  
model.summary()

  ### Training of Model ###
Adam = optimizers.Adam(lr=0.0001,  beta_1=0.9, beta_2=0.99)
model.compile(optimizer=Adam, loss="categorical_crossentropy")
history = model.fit_generator(generator=Train,steps_per_epoch=1000/batch_size, 
                    validation_data=Valid,validation_steps=200/batch_size
                    ,epochs=10)
    ### Save the model and its Weights ###
model.save('Speech_Model.h5')
model.save_weights("Speech_Model_Weights.h5")


    ## Converting the Modle to CoreML Model ###

from tensorflow.keras.models import load_model
import coremltools
    ###model = load_model('Model_.h5') ###

model.author = 'Abbas Khan'
model.short_description = 'Speech Recognition'
model.input_description['image'] = 'Takes as input an image of Constant Q-transform of audio file'
model.output_description['output'] = 'Prediction of speech'

output_labels = ['silence','Singing','Speaking']

   ###coremlModel = coremltools.converters.keras.convert(model) ###
your_model = coremltools.converters.keras.convert(model, input_names=['image'], 
                                                  output_names=['output'], 
                                                   class_labels=output_labels, 
                                                   image_input_names='image')

# =============================================================================
# your_model = coremltools.converters.tensorflow.convert(model, input_names=['image'], 
#                                                   output_names=['output'], 
#                                                    class_labels=output_labels, 
#                                                    image_input_names='image')
# =============================================================================
your_model.save('Speech_Model_ML.mlmodel')

    ### Converting the Model to TensorFLow Lite Model ###
model = load_model('Speech_Model_ML.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
print("model converted")
# Save the model.
with open('Speech_Model_TFLite.tflite', 'wb') as f:
  f.write(tflite_model)


















