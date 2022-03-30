days=[]
days.append('Lunes')
days.append('Martes')
days.append('Miércoles')
days.append('Jueves')
days.append('Viernes')
days.append('Sábado')
days.append('Domingo')

print(days) #Días completos.

x=days.pop()  #Días sin Domingo
print(days)

x=days.pop()  #Días sin Domingo, Sábado
print(days)

x=days.pop()  #Días sin Domingo, Sábado, Viernes
print(days)

x=days.pop()  #Días sin Domingo, Sábado, Viernes, Jueves
print(days)

x=days.pop()  #Días sin Domingo, Sábado, Viernes, Jueves, Miércoles
print(days)

x=days.pop()  #Días sin Domingo, Sábado, Viernes, Jueves, Miércoles, Martes.
print(days)

x=days.pop()  #Ningún día
print(days)