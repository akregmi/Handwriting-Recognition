
import matplotlib.pyplot as plt
# import tensorflow as tf
from tensorflow import keras
import numpy as np


# From Keras, load the MNIST digits classification dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Visualize the first 10 instances (digits) from the dataset
plt.figure(figsize=(5,2))
for i in range(10):
    plt.subplot(5, 2, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.axis('off')  
plt.show()

# Verify the shape of the instances and associated label
print("In the training set, there are", len(x_train), "instances (2D grayscale image data with 28×28 pixels. \
In turn, every image is represented as a 28×28 array rather than a 1D array of size 784. \
Pixel values range from 0 (white) to 255 (black).) \
The associated labels are digits ranging from 0 to 9.\n")

# Scale the input feature down to 0-1 values, by dividing them by 255.0 
x_train = x_train/255.0
x_test = x_test/255.0 

# Create a Sequential model. A sequential model is a stack of layers connected sequentially.
# This is the simplest kind of model for neural networks in Keras.
model = keras.models.Sequential()

# Build a first layer to the model, that will convert each 2D image into a 1D array. 
# For this, add a 'Flatten layer', and specify the shape (input_shape) of the instances [28,28]. 
model.add(keras.layers.Flatten(input_shape=[28,28]))

# Build the first hidden layer to the model. 
# For this, use a 'Dense layer' with 300 neurons, and use the ReLU activation function. 
# A dense Layer is simple layer of neurons in which each neuron receives input from all the neurons of previous layer.
model.add(keras.layers.Dense(300, activation="relu"))

# Build a second hidden layer to the model. 
# For this, use a 'Dense layer' with 100 neurons, also using the ReLU activation function.
model.add(keras.layers.Dense(100, activation="relu"))

# Build an output layer to the model.
# For this, use a 'Dense layer' with 10 neurons (one per class), using the softmax activation function.
model.add(keras.layers.Dense(10, activation="softmax"))

# Explain why the softmax activation function was used for the output layer.
print("The softmax action function was use for the output layer because we want to make one per class since they are exclusive\n") #5 points

# Use the model’s summary() method to display the model’s layers. Then complete the following blanks  
# (there is no need to write anycode to retrieve the information, you can simply type-in your answers directly)
print("The size of the first hidden layer is none. None means the size is unspecified and can be anything.\
The total number of parameters of the first hidden layer is 235500, which refers to the number of connection weights plus the bias terms\n") #8 points
model.summary()

# Call the method compile() on your model to specify the loss function and the optimizer to use. 
# Set the loss function to be "sparse_categorical_crossentropy" and use the stochastic gradient descent optimizer.
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd")

# Research then explain what is an epoch in machine learning.
print("An epoch is the number of times that the algorithm will work through the dataset to allow updates to the model's parameters.") #6 points

# Training the model: call the method fit(). As usual, you should pass the input features (x_train) 
# and the associated target classes (y_train). This time, also set the number of epochs to 20.
model.fit(x_train, y_train, epochs=30)


# Test the model: use the method predict() to predict the labels of the first 10 instances of the test set
plt.close('all')
y_pred = model.predict(x_test[:10])
plt.figure(figsize=(5,2))
for i in range(10):
    plt.subplot(5, 2, i + 1)
    plt.title('Predicted label: ' + str(np.argmax(y_pred[i])))
    plt.imshow(x_test[i], cmap='gray')
    plt.axis('off')  
plt.show()


