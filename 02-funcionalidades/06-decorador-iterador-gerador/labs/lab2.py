import time
import numpy as np

def time_decorator(fn):
    def fn_melhorada(*args,**kwargs):
        import time
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"função '{fn.__name__}' demorou {(end-start):0.5f}")
        return result
    
    return fn_melhorada

@time_decorator
def multiplicar_constante(c):
    lista = list(range(1_000_000))
    resultado = [x * c for x in lista]
    return resultado

@time_decorator
def multiplicar_constante_np(c):
    lista = np.array(list(range(1_000_000)))
    resultado = lista * c
    return resultado

multiplicar_constante(2)
multiplicar_constante_np(2)