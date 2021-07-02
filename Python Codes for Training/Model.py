import tensorflow.keras as keras
def Model1(input_size = (288,432,1)):
    inputs=keras.layers.Input(input_size)
     # Block 1
    x = keras.layers.Conv2D(16, (3, 3),activation='relu',padding='same',name='block1_conv1')(inputs)
    x = keras.layers.Conv2D(16, (3, 3),activation='relu',padding='same',name='block1_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)
    # Block 2
    x = keras.layers.Conv2D(32, (3, 3), activation='relu',padding='same',name='block2_conv1')(x)
    x = keras.layers.Conv2D(32, (3, 3),activation='relu',padding='same',name='block2_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)
     # Block 3
    x = keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same',name='block3_conv1')(x)
    x = keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same',name='block3_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)
    # Block 4
    x = keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same',name='block4_conv2')(x)
    x = keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same',name='block4_conv3')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)
    #x = keras.layers.Dropout(0.2)(x)
    # Block 5
    x = keras.layers.Conv2D(256, (3, 3),activation='relu',padding='same',name='block5_conv1')(x)
    x = keras.layers.Conv2D(256, (3, 3),activation='relu',padding='same',name='block5_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.Flatten(name='flatten')(x)
    
    #fully connected
    
    y= keras.layers.Dense(5000, activation='relu', name='fc4')(x)
    y=keras.layers.BatchNormalization()(y)

    y= keras.layers.Dense(1000, activation='relu', name='fc5')(y)
    y=keras.layers.BatchNormalization()(y)
    
    y= keras.layers.Dense(100, activation='relu', name='fc6')(y)
    y=keras.layers.BatchNormalization()(y)

    y = keras.layers.Dense(3, activation='softmax', name='class')(y)
    model = keras.models.Model(inputs, y)
    return model


def Model2(input_size = (288,432,1)):
    inputs=keras.layers.Input(input_size)
     # Block 1
    x = keras.layers.Conv2D(16, (7, 1),activation='relu',padding='same',name='block1_conv1')(inputs)
    x = keras.layers.Conv2D(16, (1, 7),activation='relu',padding='same',name='block1_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)
    # Block 2
    x = keras.layers.Conv2D(32, (5, 1), activation='relu',padding='same',name='block2_conv1')(x)
    x = keras.layers.Conv2D(32, (1, 5),activation='relu',padding='same',name='block2_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)
     # Block 3
    x = keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same',name='block3_conv1')(x)
    x = keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same',name='block3_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)
    # Block 4
    x = keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same',name='block4_conv2')(x)
    x = keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same',name='block4_conv3')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)
    
    x = keras.layers.Conv2D(16, (1, 1),activation='relu',padding='same',name='block5_conv3')(x)
    x=keras.layers.BatchNormalization()(x)
    
    x = keras.layers.Flatten(name='flatten')(x)
    
    #fully connected
    
    y= keras.layers.Dense(500, activation='relu', name='fc4')(x)
    #y=keras.layers.BatchNormalization()(y)

    y= keras.layers.Dense(100, activation='relu', name='fc5')(y)
    #y=keras.layers.BatchNormalization()(y)

    y = keras.layers.Dense(3, activation='softmax', name='class')(y)
    model = keras.models.Model(inputs, y)
    return model


def Model3(input_size = (288,432,1)):
    inputs=keras.layers.Input(input_size)
     # Block 1
    x = keras.layers.Conv2D(16, (7, 1),activation='relu',padding='same',name='block1_conv1')(inputs)
    x = keras.layers.Conv2D(16, (1, 7),activation='relu',padding='same',name='block1_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)
    # Block 2
    x = keras.layers.Conv2D(32, (5, 1), activation='relu',padding='same',name='block2_conv1')(x)
    x = keras.layers.Conv2D(32, (1, 5),activation='relu',padding='same',name='block2_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)
     # Block 3
    x = keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same',name='block3_conv1')(x)
    x = keras.layers.Conv2D(64, (3, 3),activation='relu',padding='same',name='block3_conv2')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)
    # Block 4
    x = keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same',name='block4_conv2')(x)
    x = keras.layers.Conv2D(128, (3, 3),activation='relu',padding='same',name='block4_conv3')(x)
    x=keras.layers.BatchNormalization()(x)
    x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)
    
    x = keras.layers.Conv2D(16, (1, 1),activation='relu',padding='same',name='block5_conv3')(x)
    x=keras.layers.BatchNormalization()(x)
    
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Flatten(name='flatten')(x)
    
    #fully connected
    
    #y= keras.layers.Dense(500, activation='relu', name='fc4')(x)
    #y=keras.layers.BatchNormalization()(y)

    y= keras.layers.Dense(10, activation='relu', name='fc5')(x)
    #y=keras.layers.BatchNormalization()(y)

    y = keras.layers.Dense(3, activation='softmax', name='class')(y)
    model = keras.models.Model(inputs, y)
    return model

