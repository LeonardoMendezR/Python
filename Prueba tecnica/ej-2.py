def max_de_tres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return a 

print(max_de_tres(2, 2, 2))