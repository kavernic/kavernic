import time
import logging
from functools import wraps

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def medir_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        logging.info(f'La función {funcion.__name__} tardó {tiempo_total:.4f} segundos en ejecutarse')
        return resultado
    return wrapper

def validar_argumentos(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f'Los argumentos deben ser números. Se recibió: {type(arg)}')
        return funcion(*args, **kwargs)
    return wrapper

@medir_tiempo
@validar_argumentos
def calcular_factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0:
        return 1
    return n * calcular_factorial(n-1)

@medir_tiempo
@validar_argumentos
def calcular_fibonacci(n):
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# Ejemplos de uso
if __name__ == "__main__":
    try:
        print("\nCalculando factorial de 5:")
        print(f"Resultado: {calcular_factorial(5)}")
        
        print("\nCalculando el número de Fibonacci en la posición 10:")
        print(f"Resultado: {calcular_fibonacci(10)}")
        
        # Este ejemplo generará un error
        print("\nIntentando calcular factorial de 'abc':")
        calcular_factorial('abc')
        
    except Exception as e:
        logging.error(f"Error: {str(e)}") 