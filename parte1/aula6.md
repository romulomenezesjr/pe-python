# Repetição

Em Python, as estruturas de repetição são usadas para executar um bloco de código repetidamente enquanto uma determinada condição for verdadeira. Existem duas principais estruturas de repetição em Python: o loop "for" e o loop "while". Vou explicar cada um deles a seguir:

## FOR

O loop "for" é usado para iterar sobre uma sequência de elementos, como listas, strings, dicionários, etc. Ele percorre cada elemento da sequência e executa o bloco de código associado para cada elemento. A sintaxe básica do loop "for" é a seguinte:

```python
for elemento in sequencia:
    # Bloco de código a ser executado

```

Onde:

"elemento" é a variável que recebe cada valor da sequência em cada iteração.
"sequencia" é a coleção de elementos que queremos percorrer, como uma lista, string ou outra estrutura iterável.

Exemplo:

```python
frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)

```

O loop "for" é frequentemente utilizado em conjunto com as funções range() e enumerate() em Python para facilitar a iteração sobre sequências e obter índices durante o processo.

## Função range():

A função range() é usada para gerar uma sequência de números em um intervalo especificado. Ela pode ser usada de várias maneiras, mas a forma mais comum é com apenas um argumento, que representa o valor final da sequência (o valor inicial é assumido como 0). A sintaxe básica da função range() é a seguinte:

```python
range(início, fim, passo)

```

início: Valor inicial da sequência (opcional, o padrão é 0).
fim: Valor final da sequência (não inclusivo, ou seja, a sequência vai até fim - 1).
passo: Intervalo entre os valores da sequência (opcional, o padrão é 1).

Exemplo:

```python
for i in range(5):
    print(i)

```

Você também pode combinar o range() com o len() para iterar sobre índices de uma lista e acessar seus elementos diretamente:

```python
frutas = ['maçã', 'banana', 'laranja']

for i in range(len(frutas)):
    print(frutas[i])

```

## Função enumerate():

A função enumerate() é usada para obter tanto o índice quanto o valor de cada elemento em uma sequência. Ela retorna uma tupla contendo o índice e o valor do elemento em cada iteração. A sintaxe básica da função enumerate() é a seguinte:

```python
enumerate(sequencia)

```

Exemplo

```python
frutas = ['maçã', 'banana', 'laranja']

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

```

Podemos utilizar os índices gerados pelo enumerate() para acessar os elementos em outras partes do código durante o loop, caso seja necessário.

## Outras funções

### zip()

A função zip() é usada para combinar elementos de várias sequências em tuplas durante a iteração. Ela retorna um iterador de tuplas, onde o primeiro elemento em cada sequência é combinado para formar a primeira tupla, o segundo elemento é combinado para formar a segunda tupla e assim por diante. A iteração continua até que a sequência mais curta seja esgotada. A sintaxe básica da função zip() é a seguinte:

```python
zip(sequencia1, sequencia2, ...)

```

Exemplo:

```python
frutas = ['maçã', 'banana', 'laranja']
cores = ['vermelho', 'amarelo', 'laranja']

for fruta, cor in zip(frutas, cores):
    print(f"{fruta} é da cor {cor}")

```

### reversed():

A função reversed() é usada para inverter a ordem dos elementos em uma sequência. Ela retorna um iterador reverso que pode ser utilizado no loop "for" para percorrer a sequência de trás para frente. A sintaxe básica da função reversed() é a seguinte:

Sintaxe:

```python
reversed(sequencia)

```

Exemplo:

```python
frutas = ['maçã', 'banana', 'laranja']

for fruta in reversed(frutas):
    print(fruta)

```

### sorted()

A função sorted() é usada para ordenar elementos em uma sequência. Ela retorna uma nova lista com os elementos ordenados. Você pode usar a lista ordenada no loop "for" para iterar sobre os elementos na ordem desejada. A sintaxe básica da função sorted() é a seguinte:

```python
sorted(sequencia)

```

Exemplo:

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

for numero in sorted(numeros):
    print(numero)

```

Essas são apenas algumas das funções que podem ser usadas em conjunto com o loop "for" em Python. A linguagem oferece muitas outras funções e bibliotecas que podem tornar o trabalho com loops mais eficiente e conveniente, dependendo da tarefa que você está tentando realizar. Fique à vontade para explorar a documentação oficial do Python e outras fontes para conhecer mais sobre as opções disponíveis

# While

O loop "while" é usado para repetir um bloco de código enquanto uma condição for verdadeira. Ou seja, ele continua executando o bloco até que a condição se torne falsa. A sintaxe básica do loop "while" é a seguinte:

```python
while condição:
    # Bloco de código a ser executado

```

O bloco de código dentro do loop continuará sendo executado enquanto a "condição" for avaliada como verdadeira.

```python
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

```

Cuidado ao usar loops "while" para garantir que a condição eventualmente se torne falsa e não cause um loop infinito.
