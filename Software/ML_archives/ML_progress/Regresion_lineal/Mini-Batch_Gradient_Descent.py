import random
import numpy as np
import matplotlib.pyplot as plt

#Genero valores aleatorios de prueba para X, Y
X = 2 * np.random.rand(100, 1) 
y = 4 + 3 * X + np.random.randn(100, 1)

#Agrego columna de 1
X_b = np.c_[np.ones((100, 1)), X] # [1 x]

eta = 0.1 # Tasa de aprendizaje
n_iterations = 1000 #Numero de iteraciones
m = 100 # Numero de caracteristicas

# Inicializacion de manera aleatoria
theta = np.random.randn(2,1) 

#Se itera repetidas veces 
for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y) #Ecuacion de gradiente
    theta = theta - eta * gradients #resta los pasos

print(theta)

