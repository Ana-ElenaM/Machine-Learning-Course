import random

def generar_array(n):
    # Genera una matriz cuadrada de tamaño NxN con números aleatorios entre 0 y 9.
    array = []
    for _ in range(n):
        fila = [random.randint(0, 9) for _ in range(n)]
        array.append(fila)
    return array

def imprimir_array(array):
    # Imprime la matriz sin corchetes.
    for fila in array:
        print(*fila)

def calcular_suma_filas(array):
    # Calcula la suma de los elementos de cada fila y los almacena en una lista.
    return [sum(fila) for fila in array]

def calcular_suma_columnas(array):
    # Calcula la suma de los elementos de cada columna y los almacena en una lista.
    n = len(array)
    return [sum(array[i][j] for i in range(n)) for j in range(n)]

def imprimir_sumas(sumas_filas, sumas_columnas):
    # Calcula y muestra las sumas de cada fila y columna antes de las dos listas finales. 
    print("\nSuma de cada fila:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i + 1}: {suma}")

    print("\nSuma de cada columna:")
    for i, suma in enumerate(sumas_columnas):
        print(f"Columna {i + 1}: {suma}")

    print("\nLista de suma de cada fila:")
    print("sumas_filas =", sumas_filas)

    print("\nLista de suma de cada columna:")
    print("sumas_columnas =", sumas_columnas)

def main():
   # Incluya manejo de excepciones en caso de que el usuario ingrese un valor no válido para N
    try:
        n = int(input("Ingrese el tamaño de la matriz cuadrada (N): "))
    except ValueError:
        print("Error: Ingrese un número entero válido para N.")
        return

    if n <= 0:
        print("Error: N debe ser un número entero positivo.")
        return

    array = generar_array(n)

    print("\nArray generada:")
    imprimir_array(array)

    sumas_filas = calcular_suma_filas(array)
    sumas_columnas = calcular_suma_columnas(array)

    imprimir_sumas(sumas_filas, sumas_columnas)

if __name__ == "__main__":
    main()
