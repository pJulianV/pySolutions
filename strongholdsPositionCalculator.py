import cmath
import math
import matplotlib.pyplot as plt

def stronghold_positions(x, y, ring):
    # Limitar el número total de strongholds a 128
    total_strongholds = 128
    
    # Número de strongholds en cada anillo hasta el máximo de 128
    if ring == 1:
        num_strongholds = 3
    elif ring == 2:
        num_strongholds = 6
    elif ring == 3:
        num_strongholds = 10
    elif ring == 4:
        num_strongholds = 15
    elif ring == 5:
        num_strongholds = 21
    elif ring == 6:
        num_strongholds = 28
    elif ring == 7:
        num_strongholds = 36
    elif ring == 8:
        # El octavo anillo solo puede tener los strongholds restantes
        num_strongholds = max(total_strongholds - (3 + 6 + 10 + 15 + 21 + 28 + 36), 0)
    else:
        raise ValueError("Solo hay 8 anillos con strongholds en total.")
    
    # Convertimos las coordenadas a un número complejo
    initial_stronghold = complex(x, y)
    
    # Ángulo de rotación entre cada stronghold en radianes
    angle = 2 * math.pi / num_strongholds
    
    positions = []
    
    for i in range(num_strongholds):
        # Rotación usando números complejos
        rotated_position = initial_stronghold * cmath.exp(complex(0, angle * i))
        # Añadimos la posición a la lista
        positions.append((rotated_position.real, rotated_position.imag))
    
    return positions

def plot_stronghold_positions(x, y, ring):
    positions = stronghold_positions(x, y, ring)
    
    # Separar las coordenadas x e y
    xs = [pos[0] for pos in positions]
    ys = [pos[1] for pos in positions]
    
    # Crear el gráfico
    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys, c='blue', marker='o')
    
    # Marcar la posición inicial con un color diferente
    plt.scatter([x], [y], c='red', marker='x', label='Posición inicial')
    
    # Configuración del gráfico
    plt.title(f"Posiciones de Strongholds en el Anillo {ring}")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

# Ejemplo de uso
x = 1000
y = -850
ring = 5

plot_stronghold_positions(x, y, ring)


# Explicación del código:
# Entrada de datos:

# x, y: Coordenadas del stronghold que ya conoces en el plano.
# ring: Número del anillo donde se encuentra el stronghold.
# Cálculo:

# Convertimos las coordenadas en un número complejo para aprovechar la multiplicación y rotación de números complejos.
# Según el anillo, determinamos cuántos strongholds hay.
# Calculamos el ángulo entre cada stronghold en el anillo.
# Rotamos el número complejo inicial el número de veces necesario, multiplicándolo por un número complejo con ángulo igual al ángulo entre strongholds.
# Salida:

# El programa devuelve una lista de tuplas con las coordenadas (x, y) de cada stronghold en el anillo.
# Ejemplo de uso:
# En el ejemplo proporcionado, el stronghold inicial está en las coordenadas (1000, -850) en el primer anillo. El programa calculará las coordenadas de los otros dos strongholds en ese anillo.

# Puedes cambiar los valores de x, y y ring para adaptarlos a tus necesidades.

# Control de Límite de Strongholds: Ahora el programa considera el número máximo de strongholds posibles (128) y ajusta la cantidad de strongholds en el octavo anillo para asegurarse de no exceder ese límite.
# Validación del Anillo: Si se intenta calcular para un anillo mayor al octavo, el programa lanza una excepción (ValueError) indicando que solo existen 8 anillos con strongholds.