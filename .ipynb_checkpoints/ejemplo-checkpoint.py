# Credenciales almacenadas (en un caso real, no deberías almacenar contraseñas en texto plano)
usuario_almacenado = "usuario123"
contrasena_almacenada = "contrasena123"

# Función de validación de usuario
def validar_usuario(usuario, contrasena):
    return usuario == usuario_almacenado and contrasena == contrasena_almacenada

# Bucle para solicitar credenciales hasta que sean correctas
while True:
    usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")

    # Validar las credenciales
    if validar_usuario(usuario_ingresado, contrasena_ingresada):
        print("Acceso concedido. Bienvenido!")
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.")
        # Preguntar si el usuario desea intentar de nuevo o salir
        continuar = input("¿Desea intentar de nuevo? (s/n): ")
        if continuar.lower() != 's':
            print("Saliendo del sistema.")
            break  # Salir del bucle si el usuario no desea continuar
