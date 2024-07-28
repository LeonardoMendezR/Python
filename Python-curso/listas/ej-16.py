#Crea una lista de listas donde cada sublista contenga tres números consecutivos empezando del 1, 
# es decir, [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Recorre la lista y imprime cada sublista en una nueva línea.

lista=[]

for i in range(1,10,3):
    sublista = [i, i+1, i+2]
    lista.append(sublista)
  
print(lista)