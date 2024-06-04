''' 1. Write an example for different Python data types
 such as Number(Integer, Float, Complex),
  String, Boolean, List, Tuple, Set and Dictionary.'''

  #R/1
  # Número - Entero
num_entero = 10

# Número - Flotante
num_flotante = 3.14

# Número - Complejo
num_complejo = 2 + 3j

# Cadena de texto
str_dato = "¡Hola, mundo!"

# Booleano
bool_dato = True

# Lista
lista_datos = [1, 2, 3, 4, 5]

# Tupla
tupla_datos = (6, 7, 8, 9, 10)

# Conjunto
conjunto_datos = {1, 2, 3, 4, 5}

# Diccionario
diccionario_datos = {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York'}

# Imprimir los tipos de datos
print(type(num_entero))
print(type(num_flotante))
print(type(num_complejo))
print(type(str_dato))
print(type(bool_dato))
print(type(lista_datos))
print(type(tupla_datos))
print(type(conjunto_datos))
print(type(diccionario_datos))


'''2. Encuentra una distancia euclidiana entre (2, 3) y (10, 8)'''

'''#R/1.1
import math

# Coordenadas de los dos puntos
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculando la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia euclidiana entre los puntos ({}, {}) y ({}, {}) es: {:.2f}".format(x1, y1, x2, y2, distancia))
'''
#R/1.2

import math

# Coordenadas de los dos puntos
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculando la distancia euclidiana
distancia = math.hypot(x2 - x1, y2 - y1)

print("La distancia euclidiana entre los puntos ({}, {}) y ({}, {}) es: {:.2f}".format(x1, y1, x2, y2, distancia))