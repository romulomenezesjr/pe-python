# Repetição

As estruturas de repetição são fundamentais na programação porque permitem que você execute um conjunto de instruções várias vezes sem ter que escrever o mesmo código repetidamente. Isso economiza tempo, torna o código mais eficiente e legível, e permite que os programas lidem com tarefas repetitivas de maneira elegante.

No nosso cotidiano estamos constantemente realizando tarefas repetitivas e por vezes desejamos que o computador as faça para nós. Para calcular o total de uma lista de compras passamos para o programa uma lista de valores e ele se encarrega de somá-los um por um para obter o resultado. O governo realiza o senso a cada conjunto de anos e deve obter diversas estatíticas sobre a população (média de idade, proporção de homens/mulheres, faixa salarial) a partir das várias respostas às perguntas.

## Estruturas de Repetição em Python


Em Python, as estruturas de repetição são usadas para executar um bloco de código repetidamente enquanto uma determinada condição for verdadeira. Existem duas principais estruturas de repetição em Python: o loop "while" e o "for". 

## While

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

 De certa forma o loop while é similar à estrutura condicional if. Pois o bloco após a instrução será executado somente se a condição for verdadeira. No while o bloco vai ser executado várias vezes. Em algum ponto dentro do bloco a condição deve se tornar falsa ou então esta repetição irá se tornar um loop infinito.

Cuidado ao usar loops "while" para garantir que a condição eventualmente se torne falsa e não cause um loop infinito.

```python
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador -= 1 # Esta instrução não fará com que a condição do while seja atendida. Loop infinito.

```
O interpretador python detecta quando o código possui tal instrução e encerra o programa para que o sistema operacional que o estiver executando não trave.

### Exemplos do uso do while

#### Exemplo 1 - Fila no Supermercado:
Imagine que você está em uma fila no supermercado. Enquanto houver pessoas na fila (condição verdadeira), você continua esperando na fila e avança um passo de cada vez (executa o código dentro do while). Assim que a fila estiver vazia (condição falsa), você para de esperar.


```python
contagem_regressiva = 10

while contagem_regressiva > 0:
    print(f"Contagem regressiva: {contagem_regressiva}")
    contagem_regressiva -= 1

print("Foguete lançado!")
```

#### Exemplo 2 - Contagem Regressiva de um Foguete:
Pense em um foguete prestes a ser lançado. Enquanto a contagem regressiva não atingir zero (condição verdadeira), o lançamento é adiado e a contagem diminui a cada segundo.

```python
contagem_regressiva = 10

while contagem_regressiva > 0:
    print(f"Contagem regressiva: {contagem_regressiva}")
    contagem_regressiva -= 1

print("Foguete lançado!")
```
#### Exemplo 3 - Jogo de Advinhação

Considere um jogo de adivinhação, onde o jogador deve adivinhar um número secreto. O jogo continuará até que o jogador acerte o número secreto. 

```python
import random

# Gerar um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializar o contador de tentativas
tentativas = 0
acertou = False

# Iniciar o loop do jogo
while not acertou:
    # Solicitar ao jogador uma tentativa
    tentativa = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    
    # Incrementar o contador de tentativas
    tentativas += 1
    
    # Verificar se o jogador acertou
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativas.")
        acertou = True
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

```

 A cada iteração do loop, o jogador faz uma tentativa, e o código verifica se a tentativa é igual ao número secreto, maior ou menor. Com base nisso, fornece feedback ao jogador e atualiza o contador de tentativas.
 
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

