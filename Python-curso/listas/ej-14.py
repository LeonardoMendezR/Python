#Crea una lista con los números del 1 al 10. 
# Usa slicing para crear una nueva lista que contenga solo los números del 3 al 7 (inclusive) y luego imprímela.

lista=[]

for i in range(1,11):
    lista.append(i)

lista_nueva=lista[2:7]

print(lista_nueva)
