#Crea una lista con los números del 1 al 5. Recorre la lista e imprime cada número al cuadrado.


numbers = []

for i in range(1,6):
    numbers.append(i)
    
for i in range(1,6):
    print(numbers[i-1]**2)