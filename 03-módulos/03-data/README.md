# Módulos para análise de dados

## NumPy

### 📌 Definição
O **NumPy** é uma biblioteca Python usada para computação numérica. Ela fornece suporte para arrays multidimensionais e um grande numero funções matemáticas que manipulam estes arrays em alto desempenho. Normalmente é uma base para outras bibliotecas como pandas, SciPy, scikit-learn, etc.

Mesmo que no Python já existam as coleções e as listas, a forma como o numpy trata os arrays é mais eficiente. Utilizando dados homogêneos, implementação em baixo nível(linguagem C), tamanho fixo definido, utilização de bibliotecas otimizadas de algebra linear (pyblas e lapack) e operações paralelas e vetorização fazem a execução de funções em arrays numpy mais rápida.

---

### 📦 Instalação e utilização
 A instalação é feita utilizando o pip e a utilização é feita importando um objeto numpy, que normalmente é o renomeando para **np** por convenção.

```bash
pip install numpy
```


```py
import numpy as np
print(np.pi)
```



---

### 🔢 Criando arrays

No núcleo do pacote Numpy está a definição do objeto ndarray. Este objeto encapsula um array multidimensional e homogêneo que é utilizado para várias operações e de forma extremamente eficiente.



```python
# Array a partir de uma lista
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# Array 2D (matriz)
b = np.array([[1, 2], [3, 4]])
print(b)
```

#### Comparação de arrays e ndarray

As listas em Python também são eficientes, mas como são para uso em diversos propósitos não possuem otimizações para a computação científica. Considere o exemplo a seguir para multiplicar os elementos de uma lista **a** por elementos de uma lista **b** e salvar em outra **c**:

```py
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
```
Mesmo este código estando correto, para arrays a e b contendo milhões de números, ele tomará muito tempo. Um código na linguagem C seria mais eficiênte utilizando arrays de tamanho fixo e com dados homogêneos.

```c
for (i = 0; i < rows; i++) {
  c[i] = a[i]*b[i];
}
```
Utilizando o módulo numpy podemos fazer esta operação de forma mais simples e com a velocidade da execução da linguagem C. Internamente as operações são feitas utilizando vetorização e *broadcast*.

```py
import numpy as np
a = np.array(range(1_000_000))
b = np.array(range(1_000_000))
c = a * b
```

Observe no código a seguir a comparação de tempo para a multiplicação de um array por uma constante:

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
---

### 📐 Atributos do array


O principal objeto do NumPy é o array multidimensional homogêneo (ndarray). Ele é uma tabela de elementos (geralmente números), todos do mesmo tipo, indexados por uma tupla de inteiros não negativos. No NumPy, as dimensões são chamadas de eixos (axes). Os atributos mais importantes do objeto ndarray são:

```python
b = np.array([[1, 2], [3, 4]])
print(b.shape)       # (2, 2) - dimensões
print(b.ndim)        # 2 - número de dimensões
print(b.size)        # 4 - total de elementos
print(b.dtype)       # tipo dos dados (ex: int64)

```

---

### 🎲 Gerando arrays com funções


A função zeros cria um array preenchido com zeros, a função ones cria um array preenchido com uns, e a função empty cria um array cujo conteúdo inicial é aleatório e depende do estado da memória. Por padrão, o dtype (tipo de dado) do array criado é float64, mas isso pode ser especificado. Para criar uma sequência de números utilizados a função arange, similar à função range do python. Quando arange é usado com argumentos de ponto flutuante, geralmente não é possível prever exatamente o número de elementos obtidos, devido à precisão finita dos números em ponto flutuante. Por esse motivo, geralmente é melhor usar a função linspace, que recebe como argumento o número de elementos desejados, em vez do valor do passo.


```python
np.zeros((2, 3))         # matriz 2x3 com zeros
np.ones((3, 3))          # matriz 3x3 com uns
np.empty((3,3))          # matriz 3x3 com o conteúdo da memória (aleatório)
np.eye(3)                # matriz identidade 3x3
np.full((2, 2), 7)       # matriz 2x2 com valor 7
np.random.rand(2, 3)     # matriz aleatória 2x3 (entre 0 e 1)
np.arange(0, 10, 2)      # [0 2 4 6 8]
np.linspace(0, 1, 5)     # [0.   0.25 0.5  0.75 1. ]
```

---

### 🧮 Operações matemáticas 

Operadores aritméticos em arrays são aplicados elemento a elemento. Um novo array é criado e preenchido com o resultado. Diferentemente de muitas linguagens de matrizes, o operador de multiplicação * atua elemento a elemento em arrays NumPy. O produto matricial pode ser realizado usando o operador @ (no Python >= 3.5) ou a função/metodo dot

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)      # [5 7 9]
print(a * b)      # [4 10 18]
print(a ** 2)     # [1 4 9]

# Funções matemáticas
np.sqrt(a)        # [1.         1.41421356 1.73205081]
np.exp(a)         # exponencial
np.sin(a)         # seno

# Produto matricial (dot product)
print(np.dot(A, B))
```

Muitas operações unárias, como calcular a soma de todos os elementos do array, são implementadas como métodos da classe ndarray.

```python 
a = rg.random((2, 3))
a.sum()
a.min()
a.max()
```

#### Exemplo: média por coluna

```python
matriz = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
media_colunas = np.mean(matriz, axis=0)
print(media_colunas)  # [40. 50. 60.]
```


---

### 🔍 Indexação, fatiamento e filtro

Arrays unidimensionais podem ser indexados, fatiados (sliced) e iterados, de forma muito parecida com listas e outras sequências do Python.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

print(a[0, 1])     # 2
print(a[:, 1])     # [2 5] - todos os elementos da coluna 1
print(a[1, :])     # [4 5 6] - todos os elementos da linha 1
```

Para percorrer o array podemos utilizar a mesma estrutura de for que usamos para listas, entretanto se for necessário realizar operações em todos os elementos independentemente da forma do array podemos utilizar o atributo array.flat

```python
for row in b:
    print(row)

for element in b.flat:
    print(element)
```

É possível aplicar filtros para gerar um array novo a partir do original. Isto pode ser feito pelo operador de índice com uma expressão booleana.

```python
a = np.array([1, 2, 3, 4, 5])
print(a[a > 3])  # [4 5] - elementos maiores que 3
```

### 🔄 Alterando forma (reshape)

A forma dos arrays são os números em cada eixo.  Ela pode ser alterada com vários comandos. Note que os três comandos a seguir retornam um array modificado, mas não alteram o array original

```python
a = np.floor(10 * rg.random((3, 4)))
a.T                        # returns the array, transposed
a.ravel()                  # returns the array, flattened
a.reshape(6, 2)             # returns the array with a modified shape
```



### Referências


https://caam37830.github.io/book/index.html

https://numpy.org/doc/stable/reference/index.html




## pandas

## matplotlib