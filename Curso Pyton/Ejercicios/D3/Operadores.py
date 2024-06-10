#Declarar una variavle con un entero
edad = 26
#Declarar una variavle  con un flotante
altura = 1.78
#Declarar una variable con un numero complejo
complex = 1 + 1j

#Pedir datos a un usuario y usalos para realizar una operacion
base = float(input('Base del Triangulo:'))
altura = float(input('Alura del Triangulo:'))
area = 0.5 * base * altura
print('El area del Triangulo es:', area)


#Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).
print('Introdusca los lados de un triangulo para calcular su perimetro')
lado_a = float(input('Lado a: '))
lado_b = float(input('Lado b: '))
lado_c = float(input('Lado c: '))
perimetro = lado_a + lado_b + lado_c
print('El perimetro del triangulo es:', perimetro)

#Obtenga el largo y el ancho de un rectángulo usando el mensaje. Calcula su área y perímetro
print('Introdusca el largo y ancho del rectangulo para calcular su area y perimetro')
largo = float(input('Largo del rectangulo: '))
ancho = float(input('Ancho del rectangulo: '))
area = largo * ancho
primetro = 2 * (largo + ancho)
print('El área del rectángulo es:', area, ' y su perímetro es:', perimetro)


#Calcular el area y circurferencia de un circulo
radio = float(input('Radio del Circulo: '))
pi = 3.14
area_circulo = pi * radio * radio
circurferencia = 2 * pi * radio
print('Area del circulo es:', area_circulo, 'y su circunferencia es:', circurferencia)

#Calcula la pendiente, la intersección x y la intersección y de y = 2x -2

slope_1 = 2
intersección_x = 1
intersección_y = -2
print('pendiente:', slope_1)
print('La intersección x es:', intersección_x)
print('La intersección y es:', intersección_y)

#Encuentre la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)

import math

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2-y1) / (x2-x1)
distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('Pendiente:', slope_2)
print('Distancia:', distancia)

#Compara las pendientes de las tareas 8 y 9.

if slope_1 == slope_2:
    print('Las pendientes son iguales')
else:
    print('las pendientes no son iguales')

