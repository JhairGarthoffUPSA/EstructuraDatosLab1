#Jhair Garthoff
import os

print("""
=====================
  HIMNO CRUCEÑO!!!
=====================
""")

NOMBRE_ARCHIVO = 'himno.txt'

himno = open(NOMBRE_ARCHIVO, 'w')
himno.write('''
    Bajo el cielo más puro de América
    Y en la tierra de Ñuflo de Chávez
    Libertad van trinando las aves
    De sureste ostentando el primor

Jhair Garthoff Añez
''')
himno.close()

if NOMBRE_ARCHIVO in os.listdir("."):
    print("\nArchivo creado en la ruta: \n\n\t{0}\{1}".format(
        os.getcwd(), NOMBRE_ARCHIVO))
else:
    print("El archivo no fue creado!\n")

print("=============================================")
himno = open(NOMBRE_ARCHIVO, 'r')
contenido = himno.read()
print(contenido)

print("=============================================")
himno = open(NOMBRE_ARCHIVO, 'r')
for linea in himno:
    print(linea)
print("\n")
himno.close

print("=============================================")



#x = contenido
#print(x)

himno.close()

