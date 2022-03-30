#Ejemplo de uso Deque
from collections import deque

#Se puede inicializar con deque una lista
numbers = deque()

#Utiliza  append para ingresar valores
numbers.append(99)
numbers.append(15)
numbers.append(85)
numbers.append(50)
numbers.append(47)

#Se puede hacer pop
last_item = numbers.pop()
print(last_item) #47
print(numbers)   #deque([99, 15, 82, 50])

#O funcionar como cola
first_item = numbers.popleft()
print(first_item) #99
print(numbers)  #deque([15, 82, 50])
