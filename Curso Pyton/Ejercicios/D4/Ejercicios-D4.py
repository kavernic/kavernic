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


#Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.

#Cambie Python para todos a Python para todos usando el método de reemplazo u otros métodos.

#Divida la cadena 'Codificación para todos' usando el espacio como separador (split()).

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena por coma.

#¿Cuál es el carácter en el índice 0 en la cadena Coding For All ?

#¿Cuál es el último índice de la cadena Coding For All ?

#Qué carácter está en el índice 10 en la cadena "Codificación para todos".
#Cree un acrónimo o una abreviatura para el nombre 'Python para todos'.
#Cree un acrónimo o una abreviatura para el nombre 'Coding For All'.
#Utilice el índice para determinar la posición de la primera aparición de C en Coding For All.
#Utilice el índice para determinar la posición de la primera aparición de F en Coding For All.
#Utilice rfind para determinar la posición de la última aparición de l en Coding For All People.
#Utilice index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No se puede terminar una oración con porque porque porque es una conjunción'
#Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
#Elimina la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque es una conjunción".
#Encuentra la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
#Elimina la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque es una conjunción".
#¿''Coding For All' comienza con una subcadena Codificación ?
#¿'Codificación para todos' termina con una codificación de subcadena ?
#'Coding For All', elimina los espacios finales izquierdo y derecho en la cadena dada.
#¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier()?
# 30DíasDePython
#treinta_días_de_python
#La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacio.
