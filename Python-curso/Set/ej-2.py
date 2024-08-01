# Crea un set vacío, agrega varios elementos y luego elimina algunos de ellos.

mi_set=set()

elementos_agregar=[7,8,9,10,11]
for i in elementos_agregar:
    mi_set.add(i)
    
print(mi_set)


elements=[8,9]
for i in elements:
    mi_set.discard(i)
print(mi_set)