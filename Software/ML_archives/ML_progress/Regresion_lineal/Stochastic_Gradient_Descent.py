import random
import numpy as np
import matplotlib.pyplot as plt

#Genero valores aleatorios de prueba para X<
#Agrego columna de 1
X_b = np.c_[np.ones((100, 1)), X] # [1 x]

eta = 0.1 # learning rate
n_iterations = 1000
m = 100 #Catnidad de caracteristicas

n_epochs = 50

# learning schedule hyperparameters
t0 = 5
t1 = 50 

def learning_schedule(t):
    return t0 / (t + t1)

# Inicializacion aleatoria
theta = np.random.randn(2,1) 

for epoch in range(n_epochs):
    for i in range(m):
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1] 
        yi = y[random_index:random_index+1]
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
        eta = learning_schedule(epoch * m + i)
        theta = theta - eta * gradients

print(theta)
