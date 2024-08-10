import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def estimar_stronghold(x1, y1, x2, y2, x3, y3, x4, y4):
    # Distancias entre puntos
    dAB = calcular_distancia(x1, y1, x2, y2)
    dAC = calcular_distancia(x1, y1, x3, y3)
    dBC = calcular_distancia(x2, y2, x3, y3)
    dAD = calcular_distancia(x1, y1, x4, y4)
    dBD = calcular_distancia(x2, y2, x4, y4)

    # Aquí aplicamos la fórmula trigonométrica básica
    # Usamos el método de la ley de los cosenos para estimar las coordenadas del stronghold
    # Ejemplo básico: Asumimos que el stronghold está en la intersección de los círculos con centros en A y B
    x_stronghold = (x1 + x2 + x3 + x4) / 4
    y_stronghold = (y1 + y2 + y3 + y4) / 4

    return x_stronghold, y_stronghold

def main():
    print("Introduce las coordenadas del punto A (x1, y1):")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    print("Introduce las coordenadas del punto B (x2, y2):")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    print("Introduce las coordenadas del punto C (x3, y3):")
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))
    
    print("Introduce las coordenadas del punto D (x4, y4):")
    x4 = float(input("x4: "))
    y4 = float(input("y4: "))
    
    x_stronghold, y_stronghold = estimar_stronghold(x1, y1, x2, y2, x3, y3, x4, y4)
    
    print(f"La posición estimada del stronghold es: ({x_stronghold}, {y_stronghold})")

if __name__ == "__main__":
    main()
