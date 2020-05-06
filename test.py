# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DYurnz7y6wyU9mz2FGOIf1Hbf3RbTxoH
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.model_selection import train_test_split
import pickle
from keras.utils import np_utils
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten
import sys

fname1= sys.argv[1]
fname2= sys.argv[2]

def test_data(path_data,path_label):

  data_set=np.load(path_data)
  label_set=np.load(path_label)
  cnn_model = tf.keras.models.load_model('cnn_model')  
  
  #converting the image into a binary format
  denoise_data = []
  threshold = 120/255
  for i in range(data_set.shape[0]):
    denoise_data.append(1.0 * (data_set[i] > threshold))
  denoise_data = np.array(denoise_data)
  
  #Inverting the image 
  Invert_data = []
  threshold = 150/255
  for i in range(denoise_data.shape[0]):
    Invert_data.append(1.0 * (denoise_data[i] < threshold))
  Invert_data = np.array(Invert_data)

  #Reshaping the data to (300,300,1)
  data_input = Invert_data.reshape((Invert_data.shape[0], Invert_data.shape[1], Invert_data.shape[2], 1)).astype('float32')

  #predictions, using the pre-trained model
  prediction = cnn_model.predict(data_input)
  Y_prediction=[]
  for i in range(prediction.shape[0]):
    Y_prediction.append(np.argmax(prediction[i]))

  #Evalutaing the accuracy using the label set
  label_input=np_utils.to_categorical(label_set)
  val_loss,val_acc=cnn_model.evaluate(data_input,label_input)

  return Y_prediction,val_acc

prediction,accuracy = test_data(fname1,fname2)
print("Prediction")
print(prediction)
print('Accuracy : '+str(accuracy))