# Diccionarios

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


person = {
    'first_name':'Aysel',
    'last_name':'Caballero',
    'age':27,
    'country':'Cuba',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

'''El diccionario anterior muestra que un valor podría ser cualquier 
tipo de datos: cuerda, booleano, lista, tuple, conjunto o diccionario.'''
print(dct)
print(person)


# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

'''
Acceso a artículos de Diccionario

Podemos acceder a los artículos del Diccionario
refiriéndose a su nombre clave.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
'''

print(person['first_name']) # Aysel
print(person['country'])    # Cuba
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#print(person['city'])       # Error

'''
Eliminar la clave y los pares de valores de un diccionario

    pop(key): elimina el elemento con el nombre de la tecla especificado:
    popitem(): elimina el último elemento
    del : elimina un elemento con nombre clave especificado

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

'''

'''
Cambio del diccionario a una lista de artículos

El método ítems() cambia el diccionario a una lista de tuples.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

Despejando un diccionario

Si no queremos los artículos en un diccionario podemos limpiarlos usando método transparente().

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

Suprimiendo un diccionario

Si no utilizamos el diccionario podemos borrarlo completamente

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

Copia un diccionario

Podemos copiar un diccionario usando un método de copia. Usando copia podemos evitar la mutación del diccionario original.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

Obstando las claves del diccionario como listado

El método de las llaves nos da todas las claves de un diccionario como lista.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

Conseguir valores de diccionario en su lista de valores

El método de valores nos da todos los valores de un diccionario como lista.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

'''

