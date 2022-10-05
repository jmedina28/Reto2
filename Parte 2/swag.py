from keras.models import Sequential
from keras.layers import Dense
import numpy
import matplotlib.pyplot as plt

num = int(input("¿Cuantas veces quieres entrenar la red neuronal?\n"))
tamaño = int(input("¿Cuantas veces quieres ejecutar el entreno de la red neuronal?\n"))
sem = int(input("¿Cual es la semilla de la red neuronal?\n"))