class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario} USD"

# Gerente hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def aprobar_vacaciones(self, empleado):
        return f"El gerente {self.nombre} ha aprobado las vacaciones de {empleado}."

# Crear objetos
empleado1 = Empleado("Carlos", 2000)
gerente1 = Gerente("Laura", 5000, "Ventas")

print(empleado1.mostrar_info())  
print(gerente1.mostrar_info())  
print(gerente1.aprobar_vacaciones("Ana"))

empleado1.nombre = "Aysel Ayselova"
empleado1.salario = 8000
print(empleado1.mostrar_info())
print(gerente1.aprobar_vacaciones("Aysel Ayselova"))


"""🎯 Tarea sobre Herencia
Crea una clase Animal con un método hacer_sonido().
Luego, crea clases Perro y Gato que hereden de Animal y tengan su propio sonido.

📌 Cuando lo tengas, me lo mandas para revisión.
"""
class Animal:
    def hacer_sonido(self):
        return "El animal hace un sonido."

class Perro(Animal):
    def hacer_sonido(self):
        return "El perro ladra."

class Gato(Animal):
    def hacer_sonido(self):
        return "El gato maulla."
    
prueba_perro = Perro()
prueba_gato = Gato()    
print(prueba_perro.hacer_sonido())
print(prueba_gato.hacer_sonido())
