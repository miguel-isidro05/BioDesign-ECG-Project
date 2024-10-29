import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Datos de entrenamiento(valores reales)
X = 2 * np.random.rand(100, 1) 
y = 4 + 3 * X + np.random.randn(100, 1)

#Importo funcion de regresion lineal se basa en scipy.linalg.lstsq()
lin_reg = LinearRegression()

#Se entrena con los valores de X y y dados
lin_reg.fit(X, y)

#Valores de interceptos y coeficiente:
print(lin_reg.intercept_)
print(lin_reg.coef_)

#Valores a predecir
X_new = np.array([[0], [2]]) 
print(lin_reg.predict(X_new))
