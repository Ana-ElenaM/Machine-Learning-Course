import random

def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = [random.randint(0, 9) for _ in range(n)]
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def calcular_suma_filas(matriz):
    return [sum(fila) for fila in matriz]

def calcular_suma_columnas(matriz):
    n = len(matriz)
    return [sum(matriz[i][j] for i in range(n)) for j in range(n)]

def imprimir_sumas(sumas_filas, sumas_columnas):
    print("\nSuma de cada fila:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i + 1}: {suma}")

    print("\nSuma de cada columna:")
    for i, suma in enumerate(sumas_columnas):
        print(f"Columna {i + 1}: {suma}")

def main():
    try:
        n = int(input("Ingrese el tamaño de la matriz cuadrada (N): "))
    except ValueError:
        print("Error: Ingrese un número entero válido para N.")
        return

    if n <= 0:
        print("Error: N debe ser un número entero positivo.")
        return

    matriz = generar_matriz(n)

    print("\nMatriz generada:")
    imprimir_matriz(matriz)

    sumas_filas = calcular_suma_filas(matriz)
    sumas_columnas = calcular_suma_columnas(matriz)

    imprimir_sumas(sumas_filas, sumas_columnas)

