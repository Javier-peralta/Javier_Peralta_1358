class Array2D:
    def __init__(self, rows, cols):
        self.__data=[]
        self.__rows=rows
        self.__cols=cols
        for i in range(rows):
            tmp=[]
            for j in range(cols):
                tmp.append(None)
            self.__data.append(tmp)

    def to_string(self):
        for j in range(self.__cols):
            print(self.__data[j])

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def clearing(self,value):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__data[i][j]=value

    def set_item(self,row,col,value):
        if row>=0 and row<=self.__rows and col>=0 and col<=self.__cols:
            self.__data[row][col]=value
        else:
            return "Error en parámetros"

    def get_item(self,row,col):
        if row>=0 and row<self.__rows and col>=0 and col<self.__cols:
            return self.__data[row][col]
        else:
            return "Error en parámetros"
    
def main():
    arreglo = Array2D    
main()
