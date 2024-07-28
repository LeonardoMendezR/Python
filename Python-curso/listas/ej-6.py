#Crea una lista con los números del 1 al 5. Elimina el tercer elemento y luego imprime la lista.

numbers = []

for i in range(1,6):
    numbers.append(i)
print(numbers)

numbers.remove(3)

print(numbers)