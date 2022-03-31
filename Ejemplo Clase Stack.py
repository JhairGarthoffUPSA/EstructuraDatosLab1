class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s = Stack() #Creando un objeto de la clase Stack.
n = int(input("Ingrese la cantidad de números que desea ingresar: "))

for i in range(n):
    x=int(input("Ingrese un número: "))
    s.push(x)

if s.isEmpty() == False:
    for i in range(n):
        y=s.pop()
        print(y)

print(s.isEmpty()) #True o False

#s.push(100) #Adiciona un valor (100)
#s.push(200) #Adiciona un valor (200)

#if (Stack==[]):
#    print("El Stack ya está vacío.")

#else:
#    s.pop()    

s.size()    #Muestra el tamaño (1)

