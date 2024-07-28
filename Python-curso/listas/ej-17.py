#Escribe una función flatten que reciba una lista anidada (lista de listas) y retorne una lista plana, 
# es decir, una lista con todos los elementos en una sola dimensión.
def flatten(lista_anidada):
    lista_plana=[]
    for sublista in lista_anidada:
        for elemento in sublista:
            lista_plana.append(elemento)
    return lista_plana

lista_anidada =[[1,2,3], [4,5,6], [7,8,9]]
lista_plana=flatten(lista_anidada)
print(lista_plana)