class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_actual = 0  # Inicialmente el coche está detenido

    def acelerar(self, cantidad):
        self.velocidad_actual += cantidad
        return f"El coche ha acelerado a {self.velocidad_actual} km/h."

    def frenar(self, cantidad):
        self.velocidad_actual -= cantidad
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        return f"El coche ha frenado a {self.velocidad_actual} km/h."

    def mostrar_estado(self):
        return f"{self.marca} {self.modelo} ({self.color}), Velocidad: {self.velocidad_actual} km/h"

# Creando un objeto
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Probando métodos
print(mi_coche.mostrar_estado())  # Estado inicial
print(mi_coche.acelerar(50))      # Aceleramos
print(mi_coche.frenar(20))        # Frenamos
print(mi_coche.mostrar_estado())  # Estado final

mi_coche2 = Coche("Lada", "Niva", "Blanco")
# Probando métodos  
print(mi_coche2.mostrar_estado())  # Estado inicial
print(mi_coche2.acelerar(60))      # Aceleramos
print(mi_coche2.frenar(10))        # Frenamos
print(mi_coche2.mostrar_estado())  # Estado final

#Mi solucion
# class Libro:
#     def __init__(self, titulo, autor, num_paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.num_paginas = num_paginas
    
#     def leer(self, paginas):
#         if paginas <= self.num_paginas:
#             paginas_leidas = paginas
#             self.num_paginas -= paginas
#             return f"He leido {paginas} páginas del libro {self.titulo} ahun me quedas {paginas_leidas} paginas por leer ."

# libro = Libro("Python", "Aysel", 200)
# print(libro.leer(50))  # Salida: He leido 50 páginas del libro Python, me quedan 150 páginas por leer.

#Solucion Correcta
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
    
    def leer(self, paginas):
        if paginas <= self.num_paginas:
            self.num_paginas -= paginas  # Restar correctamente las páginas leídas
            return f"He leído {paginas} páginas del libro '{self.titulo}'. Aún me quedan {self.num_paginas} páginas por leer."
        else:
            return f"No puedes leer {paginas} páginas, el libro solo tiene {self.num_paginas} páginas restantes."

# Probando el código
libro = Libro("Python", "Aysel", 200)
print(libro.leer(50))   # He leído 50 páginas del libro 'Python'. Aún me quedan 150 páginas por leer.
print(libro.leer(180))  # No puedes leer 180 páginas, el libro solo tiene 150 páginas restantes.
