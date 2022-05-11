#Jhair Garthoff
#Grupo 1: Sabine, Fernanda, Julián, Friedman

class Matriz:
    def __init__(self,filas,columnas):
        self.matriz=[]
        self.filas=filas
        self.columnas=columnas
        
    def matrizCero(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                self.matriz[i].append(None)
    
    def llenarMatriz(self):
        x=0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]==None:
                    z=float(input("Ingrese un número: "))
                    if z!=0:
                        self.matriz[i][j]=z
                        x+=1
                    else:
                        break
                    if self.isFull()==True or z==0:
                        break
                if self.isFull()==True or z==0:
                    break
            if self.isFull()==True or z==0:
                break
            
    def mostrarMatriz(self):
        for i in range(self.filas):
            print(self.matriz[i])
            
    def isFull(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]==None:
                    return False
        return True
    
    def Lista(self):
        x=[]
        for i in range(self.filas):
            for j in range(self.columnas):
                x.append(self.matriz[i][j])
            return x
    
    def suma(self):
        suma=0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]!=None:
                    suma=suma+self.matriz[i][j]
        return suma
    
    
    def Lista_Menor(self,n):
        x=[]
        for i in range(self.filas):
            for j in range(self.columnas):
                t=self.matriz[i][j]
                if t==None:
                    t=0
                if t<n and t!=0:
                    x.append(self.matriz[i][j])
        return x
    
    def eliminarNumero(self,n):
        k=False
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]==n:
                    self.matriz[i][j]=None
                    k=True
                if k==True:
                    break
            if k==True:
                break


m=Matriz(3,3)
m.matrizCero()
m.mostrarMatriz()
## Inciso A ##
m.llenarMatriz()
m.mostrarMatriz()
## Inciso B ##
h=int(input("Ingrese un número. Se borrará la primera instancia de él en la matriz: "))
m.eliminarNumero(h)
m.mostrarMatriz()
## Inciso C ##
k=m.suma()
print("Suma de los elementos de la matriz: ",k)
## Inciso D ##
n=int(input("Ingrese un número. Se creará una lista con los números menores que él que estén dentro de la matriz: "))
lista=m.Lista_Menor(n)
print(lista)
