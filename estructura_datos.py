# Declarar una lista
numeros = [1, 3, 6, 8, 9, 45, 90]
print(numeros)

objetos = ['Hola', 3, 4.5, True]
print(objetos)

# Acceder a valores dentro de la lista
print(objetos[1])

# Metodo para lista, append, agrega un valor a la lista
objetos.append(False)

# Metodo para eliminar elemento de la lista, pop
objetos.pop(1)

# Recorrer lista con bucle

for elemento in objetos:
    print(elemento)