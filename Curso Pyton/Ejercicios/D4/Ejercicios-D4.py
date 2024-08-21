# 1.Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.
print('Treinta' + ' ' + 'Dias' + ' ' + 'De' + ' ' + 'Python')

# 2. Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'

cadena = ['Codificación', 'Para', 'Todos']
concatenacin = ' '.join(cadena)
print(concatenacin)

# 3. Declare una variable denominada empresa y asígnele un valor inicial "Codificación para todos".

empresa = 'Codificación para todos'

# 4. Imprima la variable empresa usando print() .

print(empresa)

#Imprima la longitud de la cadena de la empresa utilizando el método len() e print() .

print(len(empresa))

#Cambie todos los caracteres a letras mayúsculas usando el método Upper() .

print(empresa.upper())

#Cambie todos los caracteres a letras minúsculas usando el método lower() .

print(empresa.lower())

#Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All .

print(empresa.capitalize().title().swapcase())

#3Corte (corte) la primera palabra de la cadena Coding For All .

cadena = "Coding For All"
palabras = cadena.split()  # Divide la cadena en palabras

if len(palabras) > 0:
    primera_palabra = palabras[0]  # Obtiene la primera palabra
    print(primera_palabra)
else:
    print("La cadena está vacía")

#Compruebe si la cadena Coding For All contiene una palabra Codificación utilizando el método index, find u otros métodos.

cadena = "Coding For All"
palabra = "Coding"

indice = cadena.find(palabra)
if indice != -1:
    print(f"La palabra '{palabra}' se encuentra en el índice {indice}")
else:
    print(f"La palabra '{palabra}' no se encuentra en la cadena")


#Reemplace la palabra codificación en la 
# cadena 'Codificación para todos' por Python.

cadena = "Coding For All"
nueva_cadena = cadena.replace("Coding", "Python")
print(nueva_cadena)


#Camarar Python para todos a Python para Todos
# usando el método de reemplazo u otros métodos.

cadena = "Coding For All"
nueva_cadena = cadena.replace("Coding", "Python").replace("todos", "Todos")
print(nueva_cadena)


#Divida la cadena 'Codificación para todos' usando el 
# espacio como separador (split()).

frase = 'Codificación para todos'
dividir = frase.split(' ')
print(dividir)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# divide la cadena por coma.

it = 'Facebook, Google, Microsoft, Apple, Oracle, Amazon'
lts_it = it.split(',')
print(lts_it)

#¿Cuál es el carácter en el índice 0 en la cadena Coding For All ?
l_cadena = 'Coding for All'
cadena_lst = list(l_cadena)
print(cadena_lst[0])

#¿Cuál es el último índice de la cadena Coding For All ?
print(cadena_lst[-1])
#Qué carácter está en el índice 10 en la cadena "Codificación para todos".
print(cadena_lst[10])
#Cree un acrónimo o una abreviatura para el nombre 'Python para todos'.
#definir la cadena
phrase = 'Python para todos'
#dividor la cadena
div_palabras = phrase.split(' ')
#creo lo variable acronimo vacia 
acronimo = ""
# Creo un bucle for para lo iteracion de la busqueda de la primera letras de las palabras
for div_palabras in div_palabras:
    acronimo += div_palabras[0].upper()
#Muestro el acronimo en consola
print('El acronimo de lo frase "{}" es : {}'.format(phrase, acronimo))


#Cree un acrónimo o una abreviatura para el nombre 'Coding For All'.



#Utilice el índice para determinar la posición 
# de la primera aparición de C en Coding For All.
texto1 = "Coding For All"
posicion_C = texto1.find('C')
print(posicion_C)  # Salida: 0


#Utilice el índice para determinar la posición 
# de la primera aparición de F en Coding For All.
posicion_F = texto1.find('F')
print(posicion_F)  # Salida: 7


#Utilice rfind para determinar la posición de la 
# última aparición de l en Coding For All People.
texto2 = "Coding For All People"
posicion_l = texto2.rfind('l')
print(posicion_l)  # Salida: 19


'''
Utilice index o find para encontrar la posición de la 
primera aparición de la palabra 'porque' en la siguiente
oración: 'No se puede terminar una oración con porque porque 
porque es una conjunción'''
oracion = 'No se puede terminar una oración con porque porque porque es una conjunción'
find_porque = oracion.find('porque')
print(find_porque) # Salida: 37

#Utilice rindex para encontrar la posición de la última aparición de la 
# palabra porque en la siguiente oración: 'No puedes terminar una oración 
# con porque porque porque es una conjunción'
last_porque = oracion.rfind('porque')
print(last_porque) # Salida: 51


#Elimina la frase "porque porque porque" en la siguiente 
# oración: "No puedes terminar una oración con porque porque porque es una conjunción".


remuve_oracion = oracion.replace('porque porque porque', '').strip()
print(remuve_oracion) # Salida: No puedes terminar una oracion con es una conjunción



#¿''Coding For All' comienza con una subcadena Codificación ?

#¿'Codificación para todos' termina con una codificación de subcadena ?

# Cadena original
cadena = " Coding  For  All "

# Subcadena a verificar
substring = "Coding"  # Cambia esto a la subcadena que desees verificar

# Verificar si comienza con la subcadena
comienza_con = cadena.startswith(substring)

# Verificar si termina con la subcadena
termina_con = cadena.endswith(substring)

# Imprimir resultados
print(f'¿"{cadena}" comienza con "{substring}"? {comienza_con}')
print(f'¿"{cadena}" termina con "{substring}"? {termina_con}')



#'Coding For All', elimina los espacios finales izquierdo y derecho en la cadena dada.
print(cadena)
print(cadena.strip())
#¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier()?
# 30DíasDePython
#treinta_días_de_python
var1 = '30DayOfPython'
var2 = 'thery_day_of_python'
print(var1.isidentifier())
print(var2.isidentifier())

#La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacio.
bibliotecas = ['Django', 'Flask', 'Botella', 'Pyramid', 'Falcon']
resultado = ' # '.join(bibliotecas)
print(resultado)


oraciones = "I am enjoying this challenge.\nI just wonder what is next."
print(oraciones)



print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")


a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # Formato a 2 decimales
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")


