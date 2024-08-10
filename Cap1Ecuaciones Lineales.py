import numpy as np

# Definir una matriz de coeficientes y un vector de resultados
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)
print("Solución del sistema:", x)


# Contenido:

# Solución de sistemas de ecuaciones lineales.
# Métodos de Gauss y Gauss-Jordan.
# Concepto de matriz y operaciones con matrices.
# Práctica programable:

# Resolución de sistemas de ecuaciones lineales: Escribe un programa en Python que implemente el método de eliminación de Gauss para resolver sistemas de ecuaciones lineales. También puedes usar NumPy para resolver estos sistemas de forma más eficiente.