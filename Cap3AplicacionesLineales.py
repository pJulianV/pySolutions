import numpy as np


def aplicar_transformacion(matriz, puntos):
    return np.dot(matriz, puntos)

# Matriz de transformación (rotación en el plano)
T = np.array([[0, -1], [1, 0]])  # Rotación de 90 grados

# Conjunto de puntos
puntos = np.array([[1, 0], [0, 1]])

# Aplicar la transformación
puntos_transformados = aplicar_transformacion(T, puntos)
print("Puntos transformados:", puntos_transformados)


# Contenido:

# Definición y ejemplos de aplicaciones lineales.
# Núcleo e imagen de una aplicación lineal.
# Matrices asociadas a aplicaciones lineales.
# Práctica programable:

# Transformaciones lineales: Implementa una transformación lineal en el plano o espacio 3D. Por ejemplo, puedes crear una función que aplique una rotación o escalado a un conjunto de puntos.