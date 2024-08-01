# Itera sobre un set y cuenta cuántos elementos contiene.

set_1={1,2,3,4,5,6,7,8,9,10}
contador=0

for i in range(len(set_1)):
    contador+=1

print(f"El set tiene {contador} elementos.")