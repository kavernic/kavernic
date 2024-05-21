# Dia_2: 30 Dias de progamacion con Python
nombre = 'Aysel'
apellido = 'Caballero'
nombre_completo = "Aysel Caballero"
pais = 'Cuba'
ciudad = 'La Habana'
edad = 26
year = 2024
its_married = True
it_true = True
is_light_on = True

estudio, mes, hace_calor = 'Programacion', 'Mayo', True

print(type(nombre))  # Imprime el tipo de dato de 'nombre'
print(type(apellido)) # Imprime el tipo de dato de 'apellido'
print(type(nombre_completo)) # Imprime el tipo de dato de 'nombre_completo'
print(type(pais)) # Imprime el tipo de dato de 'pais'
print(type(edad)) # Imprime el tipo de dato de 'edad'
print(type(its_married)) # Imprime el tipo de dato de 'its_married'
print(len(nombre)) # Imprime la longitud de 'nombre'

logitud_nombre = len(nombre)
logitud_apellido = len(apellido)
comparacion = logitud_nombre == longitud_apellido  # Compara las longitudes
print(comparacion)  # Imprime el resultado de la comparación

# Declarar las variables
num_one = 5
num_two = 4

# Suma
total = num_one + num_two

# Resta
diff = num_one - num_two

# Multiplicación
producto = num_two * num_one

# División
division = num_one / num_two

# Módulo (resto)
resto = num_two % num_one

# Exponente
exp = num_one ** num_two

# División de piso
floor_division = num_one // num_two

# Imprimir los resultados
print("Total:", total)
print("Diferencia:", diff)
print("Producto:", producto)
print("División:", division)
print("Resto:", resto)
print("Exponente:", exp)
print("División de piso:", floor_division)

import math

#  Definir el radio
radio = 30

#  I. Calcular el área
area_of_circle = math.pi * radio*2

# II. Calcular la circunferencia
circum_of_circle = 2 * math.pi * radio

#  Mostrar los resultados
print("El área del círculo es:", area_of_circle)
print("La circunferencia del círculo es:", circum_of_circle)

# III. Pedir al usuario el radio
radio_usuario = input("Ingresa el radio del círculo: ")

#  Convertir a número
radio_usuario = float(radio_usuario)

#  Calcular el área con el radio del usuario
area_usuario = math.pi * radio_usuario*2

#  Mostrar el resultado
print("El área del círculo con el radio ingresado es:", area_usuario)

# Obtener el nombre del usuario
nombre = input("Ingresa tu nombre: ")

# Obtener el apellido del usuario
apellido = input("Ingresa tu apellido: ")

# Obtener el país del usuario
pais = input("Ingresa tu país: ")

# Obtener la edad del usuario
edad = input("Ingresa tu edad: ")

# Imprimir los valores (opcional)
print("Nombre:", nombre)
print("Apellido:", apellido)
print("País:", pais)
print("Edad:", edad)




















