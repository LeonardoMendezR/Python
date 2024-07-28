#Crea una lista con los números del 1 al 5. Usa el método pop para eliminar el último elemento y luego imprime la lista.

number=[]

for i in range(1,6):
    number.append(i)
print(number)
print(number.pop())