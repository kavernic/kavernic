def cache(funcion):
    # Diccionario para almacenar los resultados
    resultados = {}
    
    def wrapper(*args, **kwargs):
        # Crear una clave única para la llamada actual
        clave = str(args) + str(kwargs)
        
        # Si el resultado ya está en caché, lo retornamos
        if clave in resultados:
            print(f"Usando resultado en caché para {funcion.__name__}{args}")
            return resultados[clave]
        
        # Si no está en caché, calculamos el resultado
        print(f"Calculando {funcion.__name__}{args}")
        resultado = funcion(*args, **kwargs)
        
        # Guardamos el resultado en caché
        resultados[clave] = resultado
        return resultado
    
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@cache
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0:
        return 1
    return n * factorial(n-1)

# Pruebas
if __name__ == "__main__":
    print("Calculando Fibonacci(10) por primera vez:")
    print(fibonacci(10))
    
    print("\nCalculando Fibonacci(10) por segunda vez (debería ser instantáneo):")
    print(fibonacci(10))
    
    print("\nCalculando Factorial(5) por primera vez:")
    print(factorial(5))
    
    print("\nCalculando Factorial(5) por segunda vez (debería ser instantáneo):")
    print(factorial(5)) 