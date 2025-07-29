## Decorador (Decorator)

### Referências

https://www.datacamp.com/tutorial/decorators-python

## Iterador (Iterador)

## Gerador (Generator)

## Exercício

Refatorar um código que compara o tempo de execução entre listas Python e arrays NumPy, utilizando funções reutilizáveis e um decorator para medir o tempo de execução de forma mais organizada.

```py
import numpy as np
import time

# Lista Python
lista = list(range(1_000_000))
start = time.time()
lista_resultado = [x * 2 for x in lista]
print("Tempo com lista:", time.time() - start)

# NumPy array
array = np.array(lista)
start = time.time()
array_resultado = array * 2
print("Tempo com NumPy:", time.time() - start)

```

1 - Crie um decorator chamado tempo que:
- Recebe uma função qualquer,
- Mede quanto tempo ela leva para ser executada,
- Exibe o tempo no terminal.

2 - Encapsule cada bloco de código (lista e NumPy) dentro de funções:

- Uma função multiplicar_constante(c) que:
- Cria uma lista com 1 milhão de números,
- Multiplica cada número por uma constante c.
- Uma função multiplicar_constante_np(c) que:
- Cria um array NumPy com os mesmos números,
- Multiplica cada elemento pela constante c.

3 - Aplique o decorator @tempo a ambas as funções e as chame passando uma constante como argumento.

