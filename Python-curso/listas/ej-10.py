# Crear una lista con los nombres
lista = ["Ana", "Juan", "Pedro", "Maria"]

# Usar una comprensión de listas para crear una nueva lista con nombres de más de 3 letras
lista_nueva = [nombre for nombre in lista if len(nombre) > 3]

# Imprimir la nueva lista
print(lista_nueva)  # Salida: ['Juan', 'Pedro', 'Maria']
