
'''
Ejercicios: Nivel 1

    Crear una tuple vacía
    Crea una tuple con nombres de tus hermanas y tus hermanos (los hermanos imaginario están bien)
    Uneste a hermanos y hermanas y asignádlo a hermanos
    Cuántos hermanos tienes?
    Modifica a los hermanos tuple y agrega el nombre de tu padre y tu madre y asignálo a los miembros de la familia.



'''
# Definimos una tupla vacía
empty_tuple = tuple()

# Definimos las tuplas de hermanos y hermanas
hermanos = ('Ramonin', 'Yanlai', "Raymond")
hermanas = ('Arletys',) # Asegúrate de que esto sea una tupla, usa la coma

# Concatenamos las tuplas
hermanos_hermanas = hermanos + hermanas

# Contamos el total de hermanos y hermanas
cant_hermanos = len(hermanos_hermanas)
print('Tengo {} hermanos y hermanas'.format(cant_hermanos))