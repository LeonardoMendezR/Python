#Crea una lista con los números del 1 al 5. Cambia el segundo elemento de la lista al número 10 y luego imprime la lista.

lista=[]

for i in range(1,6):
    lista.append(i)
    
lista[2]=10
print(lista)