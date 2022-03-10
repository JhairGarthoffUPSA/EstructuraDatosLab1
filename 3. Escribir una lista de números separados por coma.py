list = input("Ingrese los números para la lista, separados por una coma (,): ")
list=list.split(',')

print(list)

suma=0
sumsq=0

for i in list:
    suma=suma+int(i)
    sumsq += int(i)**2

n=len(list)
P = suma/n
stdev = (sumsq/n-P**2)**(1/2)
print("La media es ",P,"y la desviación típica es:",stdev)