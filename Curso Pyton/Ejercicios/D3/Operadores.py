
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

#Calcular el valor de y (y = x 2 x 6x - 9). Trate de usar 
# diferentes valores x y averiguar en qué valor x y va a ser 0

for x in range(-10, 10):
    y = 6*x**3 - 9
    if y == 0:
        print('x que produce y = 0:', x)
    else:
        print('x:', x, 'y:', y)
        

#Encuentra la longitud de 'python' y 'dragón' y haz una 
# declaración de comparación falsa.

longitud_python = len('python')
longitud_dragon = len('dragon')
comparacion = longitud_python == longitud_dragon
print('Longitud de python y dragón es igual:', comparacion)


#Uso y operador para comprobar 
# si 'on' se encuentra tanto en 'python' y 'dragon'

encontrado_on = 'on' in 'python' and 'on' in 'dragon'
print('on se encuentra en python y dragon:', encontrado_on)

#Espero que este curso no esté lleno de jerga.
# Utilícese en el operador para comprobar si la jerga está en la sentencia.
jerga = 'jerga'
sentencia = 'El curso no está lleno de jerga'
encontrado_jerga = jerga in sentencia
print('Jerga en la sentencia:', encontrado_jerga)

#Escriba un script que solicite al usuario que ingrese dos palabras 
# y verifique si la segunda palabra es un anagrama de la primera.
print('Ingrese dos palabras para verificar si la segunda es un anagrama de la primera')
palabra_1 = input('Palabra 1: ')
palabra_2 = input('Palabra 2: ')

if sorted(palabra_1) == sorted(palabra_2):
    print('La segunda palabra es un anagrama de la primera')
    
#Incluso los números son divisibles por 2 y el resto es cero. 
# Cómo se comprueba si un número está incluso o no usando python?

def es_numero_par(numero):
    return numero % 2 == 0

numero = int(input('Ingrese un número: '))
if es_numero_par(numero):
    print('El número es par')
    
#Comaque si la división de piso de 7 por 3 es 
# igual al valor convertido int de 2.7.

division_piso = 7 // 3
valor_int = int(2.7)

if division_piso == valor_int:
    print('La división de piso de 7 por 3 es igual al valor convertido int de 2.7')

#Comprobar si el tipo de '10' es igual a tipo de 10

variable_1 = 10
variable_2 = '10'

if type(variable_1) == type(variable_2):
    print('El tipo de variable_1 es igual al tipo de variable_2')
    
#Comprobar si int('9.8') es igual a 10

variable_3 = int('9.8')

if variable_3 == 10:
    print('int(\'9.8\') es igual a 10')

#Escribe un script que inscriba al usuario a introducir horas y tarifa por hora. 
# Calcular el pago de la persona?

print('Ingrese sus horas y tarifa por hora')
horas = float(input('Horas: '))
tarifa_por_hora = float(input('Tarifa por hora: '))
pago = horas * tarifa_por_hora
print('El pago es:', pago)

#Escriba un script que inscriba al usuario para introducir el número de años. Calcular el número de segundos que una persona puede vivir.
# Supongan que una persona puede vivir cien años

print('Ingrese su edad en años')
edad_anios = int(input('Edad en años: '))
edad_segundos = edad_anios * 365 * 24 * 60 * 60
print('Usted a vivido:', edad_segundos, 'segundos')

'''

    Escribe un guión de Python que muestra la siguiente tabla

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
