import os

print("\nCrear un archivo")
print("===================")

NOMBRE_ARCHIVO = 'datos.txt'

archivo = open(NOMBRE_ARCHIVO, 'w')
archivo.write('Esto es una prueba! \nEsto es otra prueba!')
archivo.close()

