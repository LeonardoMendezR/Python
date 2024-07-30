# Dada una tupla creada por un usuario, verificar si la palabra "perro" se encuentra en esa tupla.

print("ingresa el tamano de la tupla: ")

tamanio = int(input())
elementos=[]

i=0

while i < tamanio:
    print(f"Ingresa el elemento {i} de la tupla")
    elemento = input()
    elementos.append(elemento)
    i += 1

tupla = tuple(elementos)

if "perro" in tupla:
    print("La palabra 'perro' se encuentra en la tupla.")
else:
    print("La palabra 'perro' no se encuentra en la tupla.")
    
print("Tupla finala:", tupla)