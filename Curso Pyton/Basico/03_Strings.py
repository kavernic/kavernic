### Strings ####


my_string ='Mi String'
my_other_string ="Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = 'Este es un String\ncon salto de linea'
print(my_new_line_string)

my_tap_string = '\tEste es un String con tabulacion \ny salto de linea'
print(my_tap_string)

# Formato
name , surname , age = 'Aysel',  'Caballero', 27

print('Mi nomebre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nomebre es %s %s y mi edad es %d' %(name, surname, age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')


# Desempaquetado
lenguage = 'Python'
a, b, c, d, e, f = lenguage
print(a)
print(d)


# Division

lenguage_slice = lenguage[1:3]
print(lenguage_slice)

lenguage_slice = lenguage[1:]
print(lenguage_slice)

# Reversa

lenguage_reverse = lenguage[::-1]
print(lenguage_reverse)

 #Funciones

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count('t'))
print(lenguage.isnumeric())
print('1'.isnumeric())
print(lenguage.lower())






