def palindromo(frase,frase_invertida):
    if frase_invertida==frase:
        return True
    return False           
def inversa(frase):
    if len(frase)<=1:
        return frase
    else:
        return inversa(frase[1:])+frase[0]

frase="neuque" 
frase_invertida=inversa(frase)

print(palindromo(frase,frase_invertida))
