
class NodoDoble:
    
    def __init__ (self,value,siguiente,previo):
        self.data=value
        self.next=siguiente
        self.prev=previo

class ListaDoblementeEnlazada:
    def __init__ (self):
        self.__head=NodoDoble(None,None,None)
        self.__tail=NodoDoble(None,None,None)
        self.__head.next=self.__tail
        self.__tail.prev=self.__head
        self.__size=0

    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0

    def insert(self,value): #inserta al final
        if self.__size == 0:
            nuevo= NodoDoble(value,self.__tail,self.__head)
            self.__head.next=nuevo
            self.__tail.prev=nuevo
        else:
            nuevo= NodoDoble(value,self.__tail,self.__tail.prev)
            self.__tail.prev.next=nuevo
            self.__tail.prev=nuevo
            
        self.__size += 1

    def transversal(self):
        curr_Node=self.__head.next
        print("Head","->",end=" ")
        while curr_Node.next != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node=curr_Node.next
        print("Tail")

    def reverse_transversal(self):
        curr_Node=self.__tail.prev
        print("Tail","->",end=" ")
        while curr_Node.prev != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node=curr_Node.prev
        print("Head")

    def find_from_head (self,value):
        curr_Node = self.__head
        encontrado=None
        try:
            while curr_Node.data != value:
                curr_Node = curr_Node.next
                if curr_Node.data == value:
                    encontrado = curr_Node.data
        except:
            print("El valor no se encuentra en la lista")
            
        return encontrado
        

    def find_from_tail (self,value):
        curr_Node = self.__tail
        encontrado=None
        try:
            while curr_Node.data != value:
                curr_Node = curr_Node.prev
                if curr_Node.data == value:
                    encontrado = curr_Node.data
        except:
            print("El valor no se encuentra en la lista")
            
        return encontrado
        

    def remove_from_head (self,value):
        curr_Node = self.__head
        
        while curr_Node.data != value:
            curr_Node = curr_Node.next

        if curr_Node.data == value:
            next_Node=curr_Node.next
            curr_Node.prev.next=next_Node
            next_Node.prev=curr_Node.prev

    def remove_from_tail (self,value):
        curr_Node = self.__tail
        
        while curr_Node.data != value:
            curr_Node = curr_Node.prev

        if curr_Node.data == value:
            next_Node=curr_Node.next
            curr_Node.prev.next=next_Node
            next_Node.prev=curr_Node.prev

    def insert_between(self,value,predecesor,sucesor):
        pre_Node = self.__head
        while pre_Node.data != predecesor:
            pre_Node = pre_Node.next

        next_Node = self.__tail
        while next_Node.data != sucesor:
            next_Node = next_Node.prev

        if (pre_Node.data == predecesor) and (next_Node.data == sucesor):
            nuevo = NodoDoble(value,next_Node,pre_Node)
            pre_Node.next=nuevo
            next_Node.prev=nuevo                 
        
#Pruebas
            
def main():
    
    ldl=ListaDoblementeEnlazada()
    print(f"Tamaño={ldl.get_size()}")
    ldl.insert(10)
    ldl.insert(20)
    ldl.insert(30)
    ldl.insert(40)
    ldl.insert(50)
    ldl.transversal()
    ldl.reverse_transversal()
    print(ldl.find_from_head(80))
    print(ldl.find_from_head(10))
    ldl.remove_from_tail(30)
    ldl.transversal()
    ldl.insert_between(30,20,40)
    ldl.transversal()
    
main()







        
