# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:14:15 2023

@author: anael
"""

import random
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

def generar_array(n):
    # Genera una matriz cuadrada de tamaño NxN con números aleatorios entre 0 y 9.
    array = []
    for i in range(n):
        fila = [random.randint(0, 9) for i in range(n)]
        array.append(fila)
    return np.array(array), n  # Devolvemos también el valor de n

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
   # Incluyo manejo de excepciones en caso de que el usuario ingrese un valor no válido para N
    try:
        n = int(input("Ingresa el tamaño de la matriz cuadrada (N): "))
    except ValueError:
        print("Error: Ingresa un número entero válido para N.")
        return

    if n <= 0:
        print("Error: N debe ser un número entero positivo.")
        return

    array, n = generar_array(n)  # Obtenemos la matriz y el valor de n

    print("\nArray generada:")
    imprimir_array(array)

    sumas_filas = calcular_suma_filas(array)
    sumas_columnas = calcular_suma_columnas(array)

    imprimir_sumas(sumas_filas, sumas_columnas)

    arr1d = [str(i) for i in range(1, n + 1)]  # Creamos la matriz arr1d de etiquetas
    cmap = colors.ListedColormap(['blue', 'red', 'green', 'yellow', 'cyan', 'orange', 'purple', 'brown', 'white', 'grey'])

    _, ax = plt.subplots()
    for (i, j), z in np.ndenumerate(array):  # Iteramos sobre la matriz original generada
        ax.annotate('{}'.format(z), xy=(j + 0.4, i + 0.6), fontsize=15)

    ax.imshow(array, cmap=cmap, extent=(0, n, n, 0))  # Utilizamos la matriz original generada
    ax.grid(color='black', linewidth=3)

    plt.title("Matriz Generada")  # Arreglamo el título al gráfico
    plt.xlabel("Columnas")  # Etiqueta para el eje x
    plt.ylabel("Filas")  # Etiqueta para el eje y

    plt.xticks(np.arange(len(arr1d)), arr1d)
    plt.yticks(np.arange(len(arr1d)), arr1d)
    plt.show()

if __name__ == "__main__":
    main()
