def factorial(numero):
    if numero > 1:
        numero= numero*factorial(numero-1)
    return numero

numero = int(input("Ingrese el número del que desea calcular el factorial: "))
if numero == 0:
    print("El factorial de 0 es 1.")
else:
    print ("El factorial de",numero,"es",factorial(numero))
