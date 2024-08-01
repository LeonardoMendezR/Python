#Crea un diccionario vacío, agrega varias entradas y luego elimina algunas de ellas.

diccionario={}

valores={
    "a":"1",
    "b":"2",
    "c":"3"
    }
elementos_a_eliminar={"b","c"}
diccionario.update(valores)
print (diccionario)

for key in elementos_a_eliminar:
    if key in diccionario:
        del diccionario[key]

print (diccionario)