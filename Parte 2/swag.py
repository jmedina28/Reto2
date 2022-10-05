from keras.models import Sequential
from keras.layers import Dense
import numpy
import matplotlib.pyplot as plt

num = int(input("¿Cuantas veces quieres entrenar la red neuronal?\n"))
tamaño = int(input("¿Cuantas veces quieres ejecutar el entreno de la red neuronal?\n"))
sem = int(input("¿Cual es la semilla de la red neuronal?\n"))

numpy.random.seed(sem)

dataset = numpy.loadtxt("Parte 2\swag.csv", delimiter=',')

entrenamiento_datos = dataset[:, 0:8]
entrenamiento_valores = dataset[:, 8]


model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(entrenamiento_datos, entrenamiento_valores, num, tamaño)
evaluacion = model.evaluate(entrenamiento_datos, entrenamiento_valores)