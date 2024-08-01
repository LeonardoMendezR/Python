def es_vocal(caracter):
    vocales = {'a', 'e', 'i', 'o', 'u'}
    return caracter.lower() in vocales

print (es_vocal("A"))