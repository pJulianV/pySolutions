
# Abrimos el archivo de entrada y salida
with open('entrada.txt', 'r') as file_in, open('salida.txt', 'w') as file_out:
    # Leemos el archivo de entrada línea por línea
    for line in file_in:
        # Quitamos las estrellas (*) y negrillas (**) de la línea
        line = line.replace('*', '').replace('**', '')
        # Escribimos la línea modificada en el archivo de salida
        file_out.write(line)