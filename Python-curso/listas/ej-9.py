#Crea una lista con los números del 1 al 10. Usa una comprensión de listas para crear una nueva 
#lista que contenga solo los números pares.

numbers=[]

for i in range(1,11):
    numbers.append(i)
    
for i in range(2,11):
    if numbers[i-1]%2==0:
        print(numbers[i-1])
