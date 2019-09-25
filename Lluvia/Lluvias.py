from Array_3D import Array3D
import xlrd
print("cargando datos...")
lista=Array3D(36,33,13)
pais=[]
cont=0
for anio in range (1985,2020,1):
    cont=cont+1
    for estado in range (1,33,1):
        for mes in range (1,13,1):
            path= "./Precipitacion/"+str(anio)+"Precip.xls"                
            archivo=xlrd.open_workbook(filename=path)
            hoja=archivo.sheet_by_index(0)
            promedio=(hoja.cell_value(estado+1,mes))
            lista.set_item(cont,estado,mes,promedio)

print("Que año(1985-2019)?")
a=int(input())
print("Que estado(1-32)?")
b=int(input())
print("Que mes(1-12)?")
c=int(input())

a2=a-1984    
print("El promedio de centímetros cúbicos de lluvia fué de:")
lista.get_item(a2,b,c)
    



