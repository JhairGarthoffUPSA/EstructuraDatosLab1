#2. Calcular el promedio de una lista.

list = []
n = int(input("Ingrese un valor para la lista. 00 para terminar: "))

while n != 00:
    list.append(n)
    n = int(input("Ingrese un valor para la lista. 00 para terminar: "))
    
print(list)

suma = 0
for i in list:
    suma=suma+i
    
P = suma/len(list)
print("El promedio de la lista es:",P)