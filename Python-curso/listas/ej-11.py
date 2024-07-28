###Crea una lista con los números del 1 al 10. Usa el método reverse para invertir la lista y luego imprímela.

numbers=[]

for i in range(1,11):
    numbers.append(i)
print(numbers)

numbers.reverse()
print(numbers)