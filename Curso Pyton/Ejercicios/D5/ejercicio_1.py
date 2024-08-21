# Listas



# 1. Declarar una lista vacía
lst = []

# 2.Declarar una lista con más de 5 elementos
my_lst = [27, 1.77, 6, 2024, 1997]
# 3. Encuentra la longitud de tu lista
print(len(my_lst))
# 4. Obsicia el primer elemento, el elemento central y el último elemento de la lista
#primer elemento
frist_item = my_lst[0] #27
#elemento central

#print(frist_item)
mid_index = len(my_lst) // 2 
mid_item = my_lst[mid_index] # 6
#print(mid_item)

#ultimo esemento
last_item = my_lst[-1]  #1997
#print(last_item)

# 5. Declarar una lista llamada mixta, data-types, pon tu nombre, edad, altura, estado civil, dirección)

mixed_data_types =['Aysel', 27, 1.77, True, 'Habana,Cuba']

# 6. Declarar una variable de lista la nombró.Acompaña y asignar valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprima la lista usando print()

print(my_lst)
print(mixed_data_types)
print(it_companies)



# 8. Imprimir el número de empresas en la lista

num_companies = len(it_companies)

print("El número de compañias es:", num_companies) 

# 9. Imprime la primera, mediana y última empresa

# Imprime la primera, mediana y última empresa
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print("Primera empresa:", first_company)
print("Empresa central:", middle_company)
print("Última empresa:", last_company)

# 10. Imprime la lista tras modificar una de las empresas
it_companies[0] = 'Tesla'
print(it_companies)
# 11. Añadir una empresa de TI a las empresas

it_companies.append('Uber')

# 12. Insertar una empresa de TI en la mitad de la lista de empresas
mid_it_index = len(it_companies) // 2
it_companies.insert(mid_it_index, 'Facebock')


# 13. Camarar uno de los nombres de las empresas en mayúsculas (IBM excluido)

#???

# 14. Unete a las empresas con una cuerda'; '

mod_it = '; '.join(it_companies)
print(mod_it)

# 15. Comaque si existe cierta empresa en la lista de las empresas.

if 'IBM' in it_companies:
    print('IBM esta en IT Companies')

# 16. Ordenar la lista usando el método ordenar ()

it_companies.sort()
print(it_companies)
# 17. Invierte la lista en orden descendente usando el método inverso()

it_companies.reverse()
print(it_companies)
# 18. Rebanan las tres primeras empresas de la lista

top_3 = it_companies[:3]
print(top_3)


# 19. Rebanan las ultimas 3 empresas de la lista

last_3 = it_companies[-3:]
print(last_3)

# 20. Rebana de la compañi­a de TI media o empresas de la lista

mid_it = it_companies[mid_index:]
print(mid_it)
# 21. Eliminar la primera empresa de TI de la lista
print(it_companies)
it_companies.pop(0)
print(it_companies)
# 22. Eliminar la empresa de TI media o empresas de la lista

it_companies.pop(mid_index)
print(it_companies)

# 23. Eliminar la ultima empresa de TI de la lista

it_companies.pop(-1)
print(it_companies)

# 24. Eliminar todas las empresas de TI de la lista

it_companies.clear()
print(it_companies)

# 25. Destruye la lista de empresas de TI

del it_companies

# print(it_companies) #NameError: name 'it_companies' is not defined. Did you mean: 'num_companies'?

# 26. Unirse a las siguientes listas:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_back = front_end + back_end


# 27. Después de unirse a las listas en la pregunta 26.
# Copie la lista unida y ásigna una variable full-stack. 
# A continuación, inserte Python y SQL después de Redux.

full_stack = front_back.copy()
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

print(full_stack)