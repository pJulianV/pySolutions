import cmath
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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
    plt.figure(figsize=(12, 12))
    plt.scatter(xs, ys, c='blue', marker='o', label='Strongholds calculados')
    
    # Marcar la posición inicial con un color diferente
    plt.scatter([x], [y], c='red', marker='x', label='Posición inicial')
    
    # Añadir el área de margen de error (128x128 bloques)
    margin = 64
    plt.gca().add_patch(plt.Rectangle((x - margin, y - margin), 2 * margin, 2 * margin, 
                                       color='gray', alpha=0.2, label='Área de margen de error'))
    
    # Añadir margen de error alrededor de cada punto de stronghold
    for pos in positions:
        circle = plt.Circle((pos[0], pos[1]), margin, color='blue', alpha=0.2, fill=True)
        plt.gca().add_patch(circle)
    
    # Configuración del gráfico
    plt.title(f"Posiciones de Strongholds en el Anillo {ring} con Área de Margen de Error")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    
    # Ajustar formato de los ejes para mostrar coordenadas normales
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
    
    plt.show()

# Ejemplo de uso
x = -136
y = 2568
ring = 1

plot_stronghold_positions(x, y, ring)
