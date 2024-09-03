
'''
Ejercicios: Nivel 2

    Desempaquetar hermanos y padres de familiares.
    Crear frutas, verduras y productos animales tuples. Unirse a los tres tuples y asignarlo a una variable llamada food-stuffp.
    Camarar el sobre la tuple de food.stuff-tp a una lista de food-stuff-lt
    Rebanar el artículo o los artículos del medio de la lista de comida.stuff-tp tuple o food-stufflt.
    Rebana los tres primeros artículos y los últimos tres artículos de la lista de food-staff-lt
    Eliminar por completo el tuple de food.staff-tp
    Comprobar si existe un artículo en tuple:

    Comprobar si 'Estonia' es un país nórdico

    Comprobar si 'Islandia' es un país nádico

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')



'''

# 1. Desempaquetar hermanos y padres de familiares
hermanos = ('Ramonin', 'Yanlai', 'Raymond')
padres = ('Ramon', 'Aracelys')

# Desempaquetar
hermano1, hermano2, hermano3 = hermanos
padre1, madre1 = padres

print(f'Hermanos: {hermano1}, {hermano2}, {hermano3}')
print(f'Padres: {padre1}, {madre1}')

# 2. Crear frutas, verduras y productos animales tuples
frutas = ('manzana', 'banana', 'naranja')
verduras = ('zanahoria', 'lechuga', 'tomate')
productos_animales = ('leche', 'huevo', 'carne')

# Unirse a los tres tuples y asignarlo a una variable llamada food_stuff
food_stuff = frutas + verduras + productos_animales

# 3. Comparar la tupla de food_stuff a una lista de food_stuff_lt
food_stuff_lt = list(food_stuff)

# 4. Rebanar el artículo o los artículos del medio de la lista de food_stuff_lt
# Para obtener el medio, calculamos el índice
medio = len(food_stuff_lt) // 2
articulo_medio = food_stuff_lt[medio]  # Artículo del medio
print(f'Artículo del medio: {articulo_medio}')

# 5. Rebana los tres primeros artículos y los últimos tres artículos de la lista de food_stuff_lt
primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]

print(f'Tres primeros artículos: {primeros_tres}')
print(f'Tres últimos artículos: {ultimos_tres}')

# 6. Eliminar por completo la tupla de food_stuff
del food_stuff

# 7. Comprobar si existe un artículo en la tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Comprobar si 'Estonia' es un país nórdico
existe_estonia = 'Estonia' in nordic_countries
print(f'¿Estonia es un país nórdico? {existe_estonia}')

# Comprobar si 'Islandia' es un país nórdico
existe_islandia = 'Iceland' in nordic_countries
print(f'¿Islandia es un país nórdico? {existe_islandia}')
