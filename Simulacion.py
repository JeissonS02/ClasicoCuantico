import numpy as np
import matplotlib.pyplot as plt


def matrix_valida(matriz):
    num_filas, num_columnas = len(matriz), len(matriz[0])
    resultants = []

    for column in range(num_columnas):
        x = False
        for fila in range(num_filas):
            if matriz[fila][column] == 1:
                x = True
                break
        resultants.append(x)

    if False in resultants:
        return False
    else:
        return True


def matrix_action(matrix, vect):
    """Función para calcular la "acción" de una matriz sobre un vector"""
    filas_matriz, columnas_matriz = matrix.shape
    filas_vector, = vect.shape

    if columnas_matriz != filas_vector:
        return False

    result = np.zeros(filas_matriz)

    for j in range(filas_matriz):
        for k in range(columnas_matriz):
            result[j] += matrix[j, k] * vect[k]
    return result

def accion_matriz(matriz, vector):
    'Función para calcular la "acción" de una matriz sobre un vector con numeros complejos'

    filas_matriz, columnas_matriz = matriz.shape
    filas_vector, = vector.shape

    if columnas_matriz != filas_vector:
        return False

    resultado = np.zeros((filas_matriz), dtype=complex)

    for j in range(filas_matriz):
        for k in range(columnas_matriz):
            resultado[j] += matriz[j, k] * vector[k]
    return resultado


def canicas(matrix, vect, clicks):
    """Funcion que hace el experimento de las canicas"""
    if matrix_valida(matrix):
        cont = 0
        while cont < clicks:
            vect = matrix_action(matrix, vect)
            cont += 1

    return vect

def rendija(matriz, vector, clicks):
    """Funcion que hace el experimento de la doble rendija"""
    if matrix_valida(matriz):
        cont = 0
        while cont < clicks:
            vector = accion_matriz(matriz, vector)
            cont += 1
    return vector

def grafico(vect):
    """Funcion que imprime un diagrama de barras que muestre las
    probabilidades de un vector de estados. que se puede descargar
    como archivo de imagen"""
    a = len(vect)
    plt.style.use('_mpl-gallery')

    # make data:
    x = 0.5 + np.arange(a)
    y = []
    for i in range(len(vect)):
        y.append(vect[i])

    # plot
    fig, ax = plt.subplots()
    ax.bar(x, y, width=0.85, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, a), xticks=np.arange(1, a),
           ylim=(0, a), yticks=np.arange(1, a))

    plt.show()
