from sympy import Matrix

# Definir un conjunto de vectores
vectors = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calcular el rango
rank = vectors.rank()
print("Rango del conjunto de vectores:", rank)

# Verificar independencia lineal
if rank == len(vectors):
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")


# ? Verificación de independencia lineal: Crea un programa que reciba un conjunto de vectores y determine si son linealmente independientes. Esto se puede hacer verificando si el determinante de la matriz formada por los vectores es diferente de cero.

# ~ Definición de espacio vectorial.
# ~ Subespacios, independencia lineal, bases y dimensión.
# ~ Espacios generados por conjuntos de vectores.
# ~ Práctica programable:




# Normal
# ! Red 
# ? Blue 
# * Green 
# ^ Yellow 
# & Pink 
# ~ Purple 
# todo Mustard 
# // Grey