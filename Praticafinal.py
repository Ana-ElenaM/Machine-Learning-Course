import random

def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def calcular_suma_filas(matriz):
    sumas_filas = []
    for fila in matriz:
        suma_fila = sum(fila)
        sumas_filas.append(suma_fila)
    return sumas_filas

def calcular_suma_columnas(matriz):
    sumas_columnas = []
    for i in range(len(matriz[0])):
        suma_columna = sum(fila[i] for fila in matriz)
        sumas_columnas.append(suma_columna)
    return sumas_columnas

def imprimir_sumas(sumas):
    for i, suma in enumerate(sumas):
        print(f"Suma de la {'fila' if i % 2 == 0 else 'columna'} {i+1}: {suma}")

# Obtener el tamaño de la matriz
try:
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
except ValueError:
    print("Error: ¡Ingrese un número entero válido!")
    exit()

# Generar y mostrar la matriz
matriz = generar_matriz(n)
print("Matriz generada:")
imprimir_matriz(matriz)

# Calcular y mostrar la suma de filas y columnas
sumas_filas = calcular_suma_filas(matriz)
sumas_columnas = calcular_suma_columnas(matriz)
print("\nSuma de filas y columnas:")
imprimir_sumas(sumas_filas + sumas_columnas)
