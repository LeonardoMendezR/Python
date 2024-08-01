def inversa(frase):
    if len(frase)<=1:
        return frase
    else:
        return inversa(frase[1:])+frase[0]
frase="esto es una frase" 
frase_invertida=inversa(frase)
print(frase_invertida)