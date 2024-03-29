""" Obtencion de nodos (11 y 21, equispaciados y de Chebysheb)"""

import numpy as np
import numpy.polynomial.chebyshev as cheb
import matplotlib.pyplot as plt

def vectorize_functions(functions):
    my_functions_vec = [0] * len(functions)
    i = 0
    for function in functions:
        my_functions_vec[i] = np.vectorize(function)
        i = i + 1
    return my_functions_vec

def obtain_f_n (my_functions_vec, x):
    """ Funcion que obtiene los valores de f(x) para una funcion dada """
    f_n = [0] * len(my_functions_vec)
    i = 0
    for my_function_vec in my_functions_vec:
        f_n[i] = my_function_vec(x[i])
        i = i + 1
    return f_n

def obtencion_nodos_eq(start, stop, n_points_vec):
    """ Funcion que obtiene los nodos equiespaciados en un dominio dado para diferentes numero de puntos """
    step_vec = [[0] * len(start) for i in range(len(n_points_vec))]
    x_eq_vec = [[[0] * n_points_vec[i] for j in range(len(start))] for i in range(len(n_points_vec))]
    i = 0
    for n_points in n_points_vec:
        for j in range(len(start)):
            step_vec[i][j] = (stop[j] - start[j])/(n_points - 1)
            x_eq_vec[i][j] = np.arange(start[j], stop[j] + step_vec[i][j], step_vec[i][j])
        i = i + 1
    return x_eq_vec


def obtencion_nodos_cheb(start, stop, n_points_vec):
    """ Funcion que obtiene los nodos de Chebysehev en un dominio dado para diferentes numero de puntos """
    coeffs_cheb = [0] * len(n_points_vec)
    T_n = [[[0] * n_points_vec[i] for j in range(len(start))] for i in range(len(n_points_vec))]
    x_cheb_vec = [[[0] * n_points_vec[i] for j in range(len(start))] for i in range(len(n_points_vec))]
    i = 0
    for n_points in n_points_vec:
        for j in range(len(start)):
            coeffs_cheb[i] = [0]*n_points_vec[i] + [1]
            T_n[i][j] = cheb.Chebyshev(coeffs_cheb[i], [start[j], stop[j]])
            x_cheb_vec[i][j] = T_n[i][j].roots()
        i = i + 1
    return x_cheb_vec

def muestra_nodos(x, f_n, x_eq_vec, y_n_eq_points, title):
    """ Funcion que muestra los plots de la obtencion de los nodos """
    fig, ax = plt.subplots(len(x_eq_vec), len(y_n_eq_points[0]))
    fig.subplots_adjust(hspace=0.2, wspace=0.2)
    fig.set_size_inches(16,10)
    for i in range(len(x_eq_vec)):
        for j in range(len(y_n_eq_points[0])):
            ax[i, j].plot(x[j], f_n[j])
            ax[i, j].plot(x_eq_vec[i][j], y_n_eq_points[i][j], "o")  
            ax[i, j].tick_params(labelsize=12)
            if i == 0:
                ax[i, j].set_title("Función " + str(j + 1) + ". Nodos: 11.", fontsize=12)
            elif i == 1:
                ax[i, j].set_title("Función " + str(j + 1) + ". Nodos: 21.", fontsize=12)
    fig.suptitle(title, fontsize = 22)
    plt.show()