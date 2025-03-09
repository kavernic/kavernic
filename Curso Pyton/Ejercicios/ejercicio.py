username = input("Cual es su Nombre:")
password = input("Cual es tu contraseña:")
password_len = len(password)
pass_con = "*" * password_len
print(f"{username} tu contrasena{pass_con} tene {password_len} caracteres")