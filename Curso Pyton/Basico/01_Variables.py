# Variables

my_vaiable = "My Sreing Variable"
print(my_vaiable)

my_int_variable = 5
print(my_int_variable)


print("Este es el valor de:", my_int_variable)

# Algunas Funciones del sistema
print(len(my_vaiable))

# Variables en una sola linea 
name, surname, age = "Aysel", "Caballero", 26
print("Me llamo:", name, surname, ". Mi edad es:", age)


# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 26
age = "Aysel"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))