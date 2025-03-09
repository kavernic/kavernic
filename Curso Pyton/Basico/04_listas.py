### Listas

#synhax
my_list = list()
my_other_list = []

print(my_list)
print(len(my_list))

my_list = [35, 42, 22, 82]

print(my_list)
print(len(my_list))

my_other_list = [27, 1.77, 'Aysel', 'Caballer', 'Cuba'] # list containing different data types

age, height, address, surname, contry = my_other_list
print(age)
print(contry)
print(my_other_list[3])
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[4])
print(my_other_list[-1])
print(my_other_list[0])
print(my_list.count(35))

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# Modificar listas

fruits[3] = 'avocado'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'appel'
print(fruits)

# Comprobar listas

does_exist = 'Potato' in vegetables
print(does_exist)
exist = 'banana' in vegetables
print(exist)

# add items to a list

'''
syntax
lst = list()
lst.append(item)
'''
web_techs.append('Python')
print(web_techs)

# insert items in a list

'''
syntax
lst= ['item1', 'item2']
lst.insert(index, item)
'''

countries.insert(3, 'UK')
countries.insert(1, 'US')
print(countries)


# Eliminar articulos de una lista
''''
syntax
lst =['item1', 'item2']
lst.remove(item)
'''

countries.remove('US')
print(countries)

# Metodo pop()
'''
lst = ['item1', 'item2']
lst.pop()  #last item
lst.pop(index)
'''
web_techs.pop()
print(web_techs)
pop_element = web_techs.pop(4)
print(pop_element)
print(web_techs)

# syntax
'''lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
'''
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
#print(fruits)       # This should give: NameError: name 'fruits' is not defined

'''
# syntax
lst = ['item1', 'item2']
lst.clear()
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # [] 


'''
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon'] 