class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo} USD"
        return "Cantidad inválida."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Saldo restante: {self.__saldo} USD"
        return "Fondos insuficientes."

    def mostrar_saldo(self):
        return f"Saldo disponible: {self.__saldo} USD"

# Creando cuenta y probando métodos
cuenta = CuentaBancaria("Luis", 500)
print(cuenta.mostrar_saldo())  # Saldo inicial
print(cuenta.depositar(300))   # Depósito
print(cuenta.retirar(600))     # Retiro válido
print(cuenta.retirar(500))     # Retiro inválido
#print(cuenta.__saldo)         # Error: atributo privado


#Tarea Solucion
"""🎯 Tarea sobre Encapsulamiento
Crea una clase CajaFuerte con __clave privada.
Debe tener un método abrir_clave(clave_ingresada) que permita abrir la caja solo si la clave es correcta.

📌 Cuando lo tengas, revísalo conmigo.

"""
# class CajaFuerte:
#     def __init__(self, clave):
#         self.__clave = clave

#     def abrir_caja(self, clave_ingresada):
#         if clave_ingresada == self.__clave:
#             return "Caja abierta."
#         return "Clave incorrecta."

# caja = CajaFuerte("1234")
# print(caja.abrir_caja("1234"))  # Clave correcta
# print(caja.abrir_caja("0000"))  # Clave incorrecta
# #print(caja.__clave)             # Error: atributo privado

#Código mejorado con más funcionalidad
class CajaFuerte: 
    def __init__(self, clave):
        self.__clave = clave
        self.__intentos_restantes = 3  # Número máximo de intentos

    def abrir_caja(self, clave_ingresada):
        if self.__intentos_restantes == 0:
            return "Caja bloqueada por intentos fallidos."
        
        if clave_ingresada == self.__clave:
            self.__intentos_restantes = 3  # Reinicia los intentos al abrir con éxito
            return "✅ Caja abierta correctamente."
        else:
            self.__intentos_restantes -= 1
            return f"❌ Clave incorrecta. Intentos restantes: {self.__intentos_restantes}"

    def cambiar_clave(self, clave_actual, nueva_clave):
        if clave_actual == self.__clave:
            self.__clave = nueva_clave
            return "🔑 Clave cambiada con éxito."
        return "❌ No puedes cambiar la clave: clave actual incorrecta."

# Pruebas
caja = CajaFuerte("1234")
print(caja.abrir_caja("0000"))  # ❌ Clave incorrecta
print(caja.abrir_caja("0000"))  # ❌ Clave incorrecta
print(caja.abrir_caja("0000"))  # ❌ Clave incorrecta, último intento
print(caja.abrir_caja("1234"))  # ✅ Caja bloqueada por intentos fallidos
print(caja.cambiar_clave("1234", "5678"))  # ❌ No puedes cambiar la clave
caja2 = CajaFuerte("1233")
print(caja2.cambiar_clave("1233", "5678"))  # 🔑 Clave cambiada con éxito
print(caja2.abrir_caja("1233"))  # ❌ Clave incorrecta
print(caja2.abrir_caja("5678"))  # ✅ Caja abierta correctamente    