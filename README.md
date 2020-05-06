# Handwritten_digit_CNN
###### Convolutional Neural Network model for processing 300 x 300 hand written digits and accurately classifying them into appropriate classes.

### Requirements

* Python 3.3+
* Libraries and Packages:
sys, pickle, numpy, PIL, matplotlib, tenserflow, keras.

### Usage

1.  *Training the Model* : Training the model involves converting the source data into binary formats and inverting the colours. As well as, merging the MNIST data into the dataset.
```sh
$python train.py
```
A new model named "new model" will be generated into the same directory.

2.  *Testing the Model* : 
```sh
python test.py <path_to_data_file> <path_to_labels_file>
```

### Process Description

The tasks invovled in this model can be categorized as below:
* Importing required Packages
* Reading Datasets
* Augmenting the Datasets
* Training the Model
* Testing the Model Performance

#### Importing required Packages:
Since we process image data and implement a Keras CNN model, all dependant packages are required to be imported. Essential packages include Pandas, NumPy, Keras, TensorFlow, PIL, Matplotlib, sklearn

#### Reading Datasets: 
Apart from the provided dataset, in order to generalise the model, I added 2000 images from Keras MNIST train dataset to the training set and 2000 images from MNIST test dataset to the model test set. Both datasets are read into NumPy arrays.

#### Augmenting the Datasets: 
Data Augmentation is required in multiple phases to refine the different datasets and make them consistent for processing.
* Training Dataset Pre-processing: - The provided dataset contains noisy images and is refined in two steps:
  1.  Noise Removal – The images are converted into Binary colour scale by converting all bits in the image as 0 or 1, thereby removing any noise. This is achieved by assuming a threshold of 120, meaning all pixels with value below 120 are set to 1, and 0 otherwise.
  2.  Inverting Colours – Assuming a threshold of 150, the bits are reversed to set the background for the characters as 0 (black). This way, the mean for the dataset ~ 0.
  
* MNIST Data Pre-processing: - In order to process MNIST data together with the provided dataset, it is essential to convert the MNIST images from 28x28 into 300x300. This is achieved by padding the 28x28 images to make their dimensions 100x100 and resizing the padded images to 300x300. Padding is done in order to maintain the aspect ratio of the image and avoid image blurring.

#### Training the Model: 
Once the datasets are made consistent, one final data augmentation step is required before processing the model. Channel field is added to the data arrays and the label arrays are converted into one hot encoded arrays. Multiple convolutional layers are used with “Relu” activation function to increase the learning ability of the model. Convolutional layers are followed by 2 dense layers with “Relu” activation which assist in processing the non-linear nature of data. Finally, a 10-neuron dense layer with the “Softmax” activation is used to classify the data into 10
different classes.

#### Testing the Model:
Model is validated in two phases. First, the model is tested on the model evaluation set and the parameters are adjusted to achieve higher accuracy. Next, the model is tested on the Prediction test set (unseen dataset) to gauge the accuracy of the model and its ability to generalise.
