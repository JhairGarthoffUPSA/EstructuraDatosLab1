days=[]
dayscola=[]

days.append('Lunes')
days.append('Martes')
days.append('Miércoles')
days.append('Jueves')
days.append('Viernes')
days.append('Sábado')
days.append('Domingo')

print(days) #Días completos.

l = len(days)
for i in range(l):
    x=days.pop()  
    print(days)
    dayscola.append(x)

print(dayscola)
