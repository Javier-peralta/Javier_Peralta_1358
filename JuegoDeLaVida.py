#Reglas del juego de la vida

#1.- Si una celula que se encuentra viva tiene 0 o 1 vecino muere por
#soledad para la sihuiente generacion.dinde los vecinos son las 8
#celulas que lo rodean inmediatamente.

#2.-Una celula viva que tiene dos o tres vecinos sobrevive para la
#siguiente generación.

#3.-Una celula viva que tiene cuatro o mas vecinos muere por
#sobrepoblación para la siguiente generación.

#4.-Una celula muerta con exactamente 3 vecinos vivos resulta en un
#nacimiento cuya vida empieza en la siguiente generación. Todas las
#demas celulas muertas permanecen muertas para la siguiente generación.
#1,3 2,3 2,4

from Array_2D import Array2D

class JuegoDeLaVida:
    def __init__(self,rows,cols,generaciones,poblacion_inicial):
        self.__cuadro=Array2D(rows,cols)
        self.__filas=rows
        self.__columnas=cols
        self.__generaciones=generaciones
        """
        poblacion_inicial=[[1,3],[2,2],[2,3],[2,4]]
        """
        self.__cuadro.clearing(0)
        for cell in poblacion_inicial:
            self.__cuadro.set_item(cell[0] , cell[1] , 1 )

    def to_string(self):
        self.__cuadro.to_string()

    def configure_next_generation(self,nueva_generacion):
        self.__cuadro.clearing(0)
        for cell in nueva_generacion:
            self.__cuadro.set_item(cell[0] , cell[1] , 1 )

    def set_cell_death(self,row,col):
        self.__cuadro.set_item(row,col,0)

    def set_cell_allive(self,row,col):
        self.__cuadro.set_item(row,col,1)

    def _is_live_cell(self,row,col):
        return self.__cuadro.get_item(row,col)==1

    def get_num_live_neighbors(self,row,col):
        limites = self.calcula_vecinos(row,col)
        cont=0
        for fila in range(limites[0],limites[2]+1,1):
            for cols in range(limites[1],limites[3]+1,1):
                if fila == row and cols == col:
                    pass
                else:
                    if self._is_live_cell(fila,cols):
                        cont = cont+1
        return cont
        
    def calcula_vecinos(self,y,x):
        #[y_ini,x_ini,y_fin,x_fin]
        vecinos=[y-1,x-1,y+1,x+1]
        if vecinos[0]==-1:
            vecinos[0]=0
        if vecinos[1]==-1:
            vecinos[1]=0
        if vecinos[2]==self.__filas:
            vecinos[2]=self.__filas-1
        if vecinos[3]==self.__columnas:
            vecinos[3]=self.__columnas-1
        return vecinos
    
            
        
                
def main():
    print("Juego de La Vida")
    print("________________\n")


    print("ingrese el numero de columnas del arreglo")
    c=int(input())

    print("ingrese el numero de filas del arreglo")
    r=int(input())
    
    print("¿Cuantas celulas vivas quieres agregar?")
    cell=int(input())
    inicial=[]
    
    for g in range (cell):
        print("Escribe las coordenadas de la",g+1,"° celula viva (fila,columna)")
        print("Fila")
        f=int(input())
        while f >= r:
            print("Debe ser menor al numero de filas")
            f=int(input())
            
        print("Columna")
        q=int(input())
        while q >= c:
            print("Debe ser menor al numero de columnas")
            q=int(input())
            
        inicial.append([f,q])
    print(inicial)

    print("ingrese el numero de generaciones que quieres ejecutar")
    gen=int(input())
            

    juego=JuegoDeLaVida(r,c,gen,inicial)
    lista=[]
    print("Generacion inicial")
    juego.to_string()
    
    #inicial=[[1,2],[2,1],[2,2],[2,3]]
    for i in range (gen):
        print("Generacion numero:",i+1)
        for col in range (c):
            for row in range (r):
                if juego._is_live_cell(row,col):  
                    if (juego.get_num_live_neighbors(row,col) == 0) or (juego.get_num_live_neighbors(row,col) == 1): #Primera regla
                        pass
                    
                    elif (juego.get_num_live_neighbors(row,col) == 2) or (juego.get_num_live_neighbors(row,col) == 3): #Segunda regla
                        lista.append([row,col])
                        
                    elif juego.get_num_live_neighbors(row,col) > 3: #Tercera regla
                        pass

                elif juego._is_live_cell(row,col) == False:
                    if juego.get_num_live_neighbors(row,col) == 3: #Cuarta regla
                        lista.append([row,col])


        juego.to_string()
        juego.configure_next_generation(lista)
               
        for b in range(len(lista)):
            lista.pop()
                 
main()
