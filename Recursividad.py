def factorial(n):
    if n==0:
        return 1
    else:
        return (n*factorial(n-1))

def sumalista(lst):
    if len(lst)==1:
        return lst[0]
    else:
        actual=lst.pop()
        return actual+sumalista(lst)

def main():
    print("El factorial de 5 es: ",end='') 
    print(factorial(5))
    lista=[1,2,3,4]
    print("La suma de la lista es: ",end='')
    print(sumalista(lista))
    
main()
