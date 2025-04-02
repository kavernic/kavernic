import MySQLdb

try:
    conexion = MySQLdb.connect(
        host='localhost',
        user='root',
        password='',
        db='test'
    )
    print("¡Conexión exitosa!")

except MySQLdb.Error as e:
    print("Error al conectar a MySQL: ", e)

finally:
    if 'conexion' in locals():
        conexion.close()