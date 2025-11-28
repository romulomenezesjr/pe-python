## Decorador (Decorator)

Um decorator é uma função que recebe outra função como argumento. Após sua execução  retorna uma nova função que normalmente modifica ou estende a função passada inicialmente. Eles são usados para adicionar funcionalidades extras à funções sem que modifique o princípio da responsabilidade única. 

Decoradores são aplicações dos conceitos de funções de alta ordem (HOF) e closures. Para uma demonstração simples do seu funcionamento vamos escrever algumas funções e um decorador que adicione logs e medição de desempenho.


```py
def log_decorator(fn):
    def fn_melhorada(*args, **kwargs):
        print(f"função iniciada com valores {args}")
        result = fn(*args, **kwargs)
        return result
    return fn_melhorada

@log_decorator
def soma(a,b):
    return a+b

@log_decorator
def fatorial(n):
    if n == 0:
        return 1
    if n > 0:
        return n*fatorial(n-1)

@log_decorator
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(soma(1,1))
print(fatorial(5))
print(fibonacci(5))


```
Para usar o decorador em uma função devemos adicionar um símbolo de @ seguido do nome do decorador anteriormente à função. Nos exemplos acima o decorador de log_decorator chamado sempre que a função executou.


Os decoradores são utilizados frequentemente em bibliotecas e frameworks para adicionar as funcionalidades propostas por estes: Controle de acesso, execução de códigos de de baixo nível, execução de códigos extras e etc. 

### Exercício
1 - Faça uma pesquisa em como os decoradores são usados no módulos como fastapi, flask, celery, click, sqlalchemy, entre outros.

2 - Crie um decorador para registrar o tempo que uma função toma para concluir sua execução.  Utilize o módulo da biblioca padrão **time** para marcar o tempo inicial e final. Teste para as funções a seguir e explique o resultado:

3 - Refatorar um código que compara o tempo de execução entre listas Python e arrays NumPy, utilizando funções reutilizáveis e um decorator para medir o tempo de execução de forma mais organizada.

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

## Iterador (Iterador)

Um iterador é um objeto que permite percorrer elementos iteráveis um por vez, como em um for.
Ele sabe por onde está e qual é o próximo elemento.

Para ser um iterador, temos que criar uma classe que tenha os métodos \__iter__() e \__next__()

A linguagem python usa iteradores internamente para implementações como o for

```py
for x in [1, 2, 3]:
    print(x)

## é transformado em:

iterador = iter([1, 2, 3])
while True:
    try:
        x = next(iterador)
        print(x)
    except StopIteration:
        break


```


### Criando um iterador

Um iterador é uma classe com os métodos __iter__ e __next__.

```py 
class Contador:
    def __init__(self, limite):
        self.atual = 0
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual >= self.limite:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor

for numero in Contador(5):
    print(numero)

```
## Gerador (Generator)

Python tem uma forma mais simples de criar iteradores: funções geradoras com yield.

```py
def contador(limite):
    atual = 0
    while atual < limite:
        yield atual
        atual += 1

for n in contador(5):
    print(n)

```

### Observações:

- Iteradores são consumíveis, ou seja eles só podem ser percorridos uma vez.

```py
it = iter([1, 2, 3])
next(it)  # 1
next(it)  # 2
next(it)  # 3
next(it)  
```

- for usa StopIteration para saber quando parar. Você nunca precisa mexer nele diretamente, mas precisa lançá-lo nos seus iteradores.

- 
## Exercício






### Referências

https://www.datacamp.com/tutorial/decorators-python