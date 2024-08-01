def sumar(lista):
    sumador=0
    for i in lista:
        sumador+=i
    return sumador
def multiplicador(lista):
    multiplicador=1
    for i in lista:
        multiplicador*=i
    return multiplicador

lista =[1,2,3,4]
print(sumar(lista))
print(multiplicador(lista))