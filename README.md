# Handwritten_digit_CNN
Convolutional Neural Network model for processing Hand written digits and accurately classifying them into appropriate classes.

#### Requirements

* Python 3.3+
* Libraries and Packages:
sys, pickle, numpy, PIL, matplotlib, tenserflow, keras.

#### Usage

1.  *Training the Model* : Training the model involves converting the source data into binary formats and inverting the colours. As well as, merging the MNIST data into the dataset.
```sh
$python train.py
```
A new model named "new model" will be generated into the same directory.

2.  *Testing the Model* : 
```sh
python test.py <path_to_data_file> <path_to_labels_file>
```
