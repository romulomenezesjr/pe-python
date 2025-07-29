import time
import numpy as np


def tempo(function):
    def wrapper(*args):
        t1 = time.time()
        func = function(*args)
        t2 = time.time()
        print("Tempo: " + str(t2 - t1))
        return func

    return wrapper

@tempo
def multiplicar_constante(c):
    lista = list(range(1_000_000))
    resultado = [x * c for x in lista]
    return resultado

@tempo
def multiplicar_constante_np(c):
    lista = np.array(list(range(1_000_000)))
    resultado = lista * c
    return resultado

multiplicar_constante(2)
multiplicar_constante_np(2)