import numpy as np
import matplotlib.pyplot as plt

#Sigmoid: takes a real-valued input and squashes it to range between 0 and 1 
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

#Tanh: takes a real-valued input and squashes it to the range [-1, 1] 
def tanh(z):
    num = np.exp(z) - np.exp(-z)
    denom = np.exp(z) + np.exp(-z)
    return num/denom

#ReLU: ReLU stands for Rectified Linear Unit. It takes a real-valued input and thresholds it at zero 
def relu(z):
    return np.where(z < 0.0, 0.0, z)


#generate an array of 10 random  numbers using numpy
X=np.random.rand(10)
#generate an array of shape 10x2
X=np.random.rand(10,2)



