#Simulacro de Exámen
#Jhair Garthoff Añez
class Matriz:
    
    def __init__(self,filas,columnas):
        self.matriz=[]
        self.filas=filas
        self.columnas=columnas
        
    def llenarMatriz(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                self.matriz[i].append(int(input("[%d][%d]: "%(i+1,j+1))))
                print("==============")
                
    def mostrarMatriz(self):
        for i in range:
            print(self.matriz[i])
        print("==============")
        
    def getMatriz(self):    
        return self.matriz
    def getFilas(self):
        return self.filas
    def getColumnas(self):
        return self.columnas
    def setMatriz(self, matriz):
        self.matriz=matriz
    def llenarPares(self,s):
        for i in range(50):
            if n%2==0:
                s.append(n)
                n+=1
            i+=1
        s=[]


print("""=============================================
        Bienvenido al menú de Matriz
=============================================

1. Añadir un número a la matriz.
2. Cargar matriz con sólo números pares.
3. Mostrar la cantidad de elementos de la matriz.
///
""")
op = (input("Elija una de las opciones: "))


if op=="1":
    Matriz.getMatriz
    Matriz.llenarMatriz(int(input("Ingrese el número a añadir: ")))

elif op=="2":
    Matriz.llenarPares
    
elif op=="3":
    print("La matriz tiene",len(Matriz()),"elementos.")

else:
    print("Opción inválida.")

#(>.<)