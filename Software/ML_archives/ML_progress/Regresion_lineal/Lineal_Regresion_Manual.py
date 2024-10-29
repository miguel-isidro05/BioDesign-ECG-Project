import random
import numpy as np
import matplotlib.pyplot as plt

#Genero valores aleatorios de prueba para X, Y
#x: vector de caracteristicas
#y: valor predicho
#theta: vector de parametros
#y=theta*x

#Datos de entrenamiento(valores reales)
X = 2 * np.random.rand(100, 1) 
y = 4 + 3 * X + np.random.randn(100, 1)

print(X)
print(y)

#plt.plot(X, y) #Conecta puntos para mostrar tendendencias
#plt.scatter(X, y) #Muestra puntos individuales en el gráfico en función de sus coordenadas.
#plt.show()

#Se agrega x0=1 para cada instancia para agregar parametros posteriormente
X_b = np.c_[np.ones((100, 1)), X] # [1 x]

#Ecuacion normal, linalg es matriz inversa y dot() es multiplicacion matricial
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

print(theta_best)

#Predecimos valores con el nuevo theta_best
X_new = np.array([[0], [2]]) #probamos con dos valores que queremos predecir
X_new_b = np.c_[np.ones((2, 1)), X_new]

#Multiplicamos el valor que deseamos predecir por los mejores parametros
#(Hacemos manualmente el cambio)
y_predict = X_new_b.dot(theta_best) 

print(y_predict)

plt.plot(X_new, y_predict)#linea de tendendencia entre ambos puntos
plt.plot(X, y, "b.") #punto para hacerlos puntos discretos
plt.axis([0, 2, 0, 15])
plt.show()


#eta = 0.1 # Tasa de aprendizaje
#cant_interaciones = 1000
#m = 100 #numero de valores comparados

#theta: vector de parametros
#theta = np.random.randn(2,1) # Se inicializa de manera aleatoria

#for iteration in range(cant_interaciones):
    

 #   gradiente = 2/m * X_b.T.dot(X_b.dot(theta) - y) #Valor de la gradiente de la funcion
  #  theta = theta - eta * gradiente #o = o- n*gradiente

#print("Valor de teta: ",theta)
