class MetodoPago:
    def procesar_pago(self, cantidad):
        pass  # Método vacío

class PagoTarjeta(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad} USD procesado con tarjeta."

class PagoPayPal(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad} USD procesado con PayPal."

# Usar polimorfismo
def realizar_pago(metodo, cantidad):
    print(metodo.procesar_pago(cantidad))

tarjeta = PagoTarjeta()
paypal = PagoPayPal()

realizar_pago(tarjeta, 100)
realizar_pago(paypal, 200)

class PagoCriptomonedas(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad} USD procesado con criptomonedas."
    
bitcoin = PagoCriptomonedas()
realizar_pago(bitcoin, 300) 

"""🎯 Tarea sobre Polimorfismo
Crea una clase base Transporte con un método moverse().
Luego, crea Bicicleta y Avion que sobrescriban moverse() con diferentes mensajes.

📌 Cuando lo tengas, lo revisamos juntos. 🚀"""

class Transporte:
    def moverse(self):
        return "El transporte se mueve."

class Bicicleta:
    def moverse(self):
        return "La bicicleta pedalea sobre el pavimento."

class Avion:
    def moverse(self):
        return "El avión vuela por el aire."
    

bicicleta = Bicicleta()
avion = Avion()
print(bicicleta.moverse())  
print(avion.moverse())
