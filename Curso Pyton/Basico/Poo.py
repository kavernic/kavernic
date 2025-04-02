# Creacion de clase 
class Usuario():
    #Declaraciones de Atributos 
    nombre = "Aysel"
    edad = 27
    login = "admin"   
    password = "admin"
    email = "aysel@gmail.com"
    telefono = "123456789"
    # Declaración de métodos
    def resumen(self): # self hace referencia a la instancia de clase.
        print(f'Los datos del usuarioson:\n'
            f'Nombre: {self.nombre}\n'
            f'Edad: {self.edad}\n'
            f'Login: {self.login}\n'
            f'Password: {self.password}\n'
            f'Email: {self.email}\n'
            f'Teléfono: {self.telefono}')
ay = Usuario()
ay.resumen()


class Coche():
    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4 
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False
    
#Declaracion de metodos
    def arrancar(self):
        self.is_enMarcha = True
            
    def estado(self):
        if (self.is_enMarcha == True):
            return "El ceche esta arrancado"
        else:
            return "El coche esta parado"
        
        
coche = Coche()
coche.ruedas = 6
print("El largo del coche es de ", coche.largo, "cm.")
coche.arrancar()
print(coche.estado())
print("El coche esta arrancado:", coche.arrancar())

class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        
    def __del__(self):
        print("El libro ha sido eliminado.")
        
book = Book("Python", "Aysel", 200, 100)
book.title

del book


class Persona:
    def __init__(self, nombre, edad):   
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        
        
persona = Persona("Aysel", 27)
persona.saludar()

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de Persona
        self.carrera = carrera

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Ana", 22, "Ingeniería")
print(estudiante1.presentarse())  
# Salida: Hola, me llamo Ana y tengo 22 años y estudio Ingeniería.


class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamamos al constructor de Persona
        self.salario = salario
    
    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y mi salario es de {self.salario} USD."

# Crear un objeto de la clase Empleado
empleado1 = Empleado("Carlos", 35, 5000)
print(empleado1.presentarse())


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        return f"Saldo disponible: {self.__saldo} USD"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo} USD"
        return "Cantidad inválida."
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo} USD"
        return "Cantidad inválida."
# Crear una cuenta bancaria
cuenta = CuentaBancaria("Carlos", 1000)
print(cuenta.mostrar_saldo())  # Saldo disponible: 1000 USD
print(cuenta.depositar(500))   # Depósito exitoso. Nuevo saldo: 1500 USD
print(cuenta.mostrar_saldo())  # Saldo disponible: 1500 USD
print(cuenta.retirar(200))     # Retiro exitoso. Nuevo saldo: 1300 
cuenta.__saldo = 1000000


class Perro:
    def hacer_sonido(self):
        return "Guau!"

class Gato:
    def hacer_sonido(self):
        return "Miau!"

class Vaca:
    def hacer_sonido(self):
        return "Muu!"

class Ave:
    def hacer_sonido(self):
        return "Pio!"   



# Función que usa polimorfismo
def hacer_sonido(animal):
    print(animal.hacer_sonido())

perro = Perro()
gato = Gato()

hacer_sonido(perro)  # Guau!
hacer_sonido(gato)   # Miau!

animales = [Perro(), Gato(), Vaca(), Ave()]
for animal in animales:
    hacer_sonido(animal)