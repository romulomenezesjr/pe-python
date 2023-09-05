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

O loop for em Python é comumente usado quando você sabe antecipadamente quantas vezes deseja executar um bloco de código. O loop for é frequentemente usado com um contador para iterar através de sequências, como listas, tuplas, strings e até mesmo intervalos numéricos.

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

Nesta sequencia existem 3 posições, a variável criada dentro do for 'frutas' irá receber dentro do loop cada valor. Da seguinte forma:
- Na iteração 1: fruta = 'maçã'
- Na iteração 2: fruta = 'banana'
- Na iteração 3: fruta = 'laranja'

Exemplo do for com Strings:
```python
palavra = "Python"

for letra in palavra:
    print(letra)
```
Nesta string existem 6 valores, a variável criada dentro do for 'letra' irá receber dentro do loop cada letra da string. Da seguinte forma:
- Na iteração 1: letra = 'P'
- Na iteração 2: letra = 'y'
- Na iteração 3: letra = 't'
- Na iteração 3: letra = 'h'
- Na iteração 3: letra = 'o'
- Na iteração 3: letra = 'n'


É muito comum realizarmos a repetição com uma sequência numérica, com um início, intervalo e fim. Veja o exemplo do contador de 10 à 0.


```python
numeros = (10,9,8,7,6,5,4,3,2,1,0)

for numero in numeros:
    print(numero)
print('fim')

```

Veja que neste exemplo a variável 'numero' assume cada um dos valores da sequência 'numeros' a cada iteração.  Por fim, após o bloco do for está a instrução 'print('fim')'. O que aconteceria se a instrução 'print('fim')' estiver dentro do bloco do 'for'?



### Funções com o for

O loop "for" é frequentemente utilizado em conjunto com as funções range() em Python para facilitar a iteração sobre sequências.

### Função range():

A função range() é usada para gerar uma sequência de números em um intervalo especificado. Ela pode ser usada de várias maneiras, mas a forma mais comum é com apenas um argumento, que representa o valor final da sequência (o valor inicial é assumido como 0 e o valor do incremento é assumido como 1). A sintaxe básica da função range() é a seguinte:

```python
range(início=0, passo=1, fim)

```

início: Valor inicial da sequência (opcional, o padrão é 0).
fim: Valor final da sequência (não inclusivo, ou seja, a sequência vai até fim ).
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

Pode parecer mais trabalho fazer desta forma quando poderiamos utilizar o for diretamente. Mas ao acessar os elementos pelo índice podemos alterar a lista. Veja o exemplo a seguir: 

Exemplo: Data uma lista com os valores [1,2,3,4,5], altere esta lista para que cada um dos seus elementos seja duplicado.

```python
numeros  =  [1,2,3,4,5]

for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2
print(numeros)
```

### Função enumerate():

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

Veja o exemplo do uso do enumerate no exemplo que duplica os valores da lista:

```python
numeros  =  [1,2,3,4,5]

for i,e in enumerate(numeros):
    numeros[i] = numeros[i] * 2
print(numeros)
```


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


### FOR x WHILE

É comum se questionar sobre qual das duas estruturas de repetição é mais adequada: while ou for. Costumamos dizer que depende da situação. Em geral, quando a quantidade de iterações é indeterminada, a estrutura while é uma boa alternativa. Por outro lado, quando o número de iterações é definido, a estrutura for é bastante adequada
