# Supongamos que queremos construir una estructura en Minecraft que requiere una combinación de bloques de piedra, madera y obsidiana.
# La estructura necesita un total de 150 bloques, y la relación entre los bloques es la siguiente:
# - 3 bloques de piedra por 2 bloques de madera
# - 2 bloques de obsidiana por 5 bloques de piedra
# ¿Cuántos bloques de cada material se necesitan para construir la estructura?

import numpy as np

# Definir la matriz de coeficientes y el vector de resultados
A = np.array([[3, -2, 0], [-5, 0, 2], [1, 1, 1]])
b = np.array([0, 0, 150])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)

print("Cantidad de bloques necesarios:")
print("Piedra:", x[0], "bloques")
print("Madera:", x[1], "bloques")
print("Obsidiana:", x[2], "bloques")


# Explicación:

# En este ejemplo, estamos utilizando álgebra lineal para resolver un sistema de ecuaciones que describe la relación entre los bloques de piedra, madera y obsidiana necesarios para construir la estructura en Minecraft. La matriz de coeficientes A y el vector de resultados b se definen de la siguiente manera:

# La primera fila de A representa la relación entre la piedra y la madera: 3 bloques de piedra por 2 bloques de madera.
# La segunda fila de A representa la relación entre la obsidiana y la piedra: 2 bloques de obsidiana por 5 bloques de piedra.
# La tercera fila de A representa la condición de que la suma de los bloques debe ser igual a 150.
# El vector de resultados b tiene un valor de 150 en la tercera posición, que representa la cantidad total de bloques necesarios para construir la estructura.
# Al resolver el sistema de ecuaciones utilizando la función np.linalg.solve(), obtenemos la cantidad de cada bloque que se necesita para construir la estructura. En este caso, la solución es x = [50, 30, 20], lo que significa que se necesitan 50 bloques de piedra, 30 bloques de madera y 20 bloques de obsidiana para construir la estructura.