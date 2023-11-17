1- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, o
programa deve imprimir o valor -1 
- Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
- Leia um número do teclado
- Compare se este número está na lista

2 - Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50
lançamentos.
- Crie uma lista com tamanho 50 e armazene nesta lista valores gerados aleatóriamente
- Faça uma iteração na lista para verificar quantos destes números são iguais à 6

3- Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da seguinte forma:
cada célulaé a soma dela mesma e das células anteriores. Imprima o vetor antes e depois da manipulação. Exemplo:
- Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
- Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]

4 - Dada uma lista de números, utilize map() com uma função lambda para criar uma nova lista onde cada número é multiplicado por 2, mas apenas se for maior que 5
- Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
- Utilize a função map e uma função lambda para multiplicar por 2 os números maiores que 5

5 - Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius, em seu programa o usuário deverá inserir uma sequência de valores que representam a temperatura em graus Fahrenheit, seu programa deve receber esses valores e armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco (uma string vazia). Converta todos os valores presentes na lista para graus Celsius usando a função map e imprima na tela em uma formatação amigável ao usuário.
- Utilize o while e no bloco de repetição leia dados de temperatura do usuário
- Acrescente os dados na lista
- Crie uma função para converter temperatura de Farenheint para Celcios
- Use a função map com a função e a lista
- Imprima todas os valores da nova lista

6 - A partir do dicionário de nomes e idades de pessoas a seguir, faça um programa que imprima em ordem a partir dos nomes das pessoas, mostre a soma das idades, a média das idades e a pessoa mais velha. 
```py
people = {
    "Rafael": 41,
    "Anne": 28,
    "Jen": 32,
    "Satan": 2000000,
    "Frank": 12,
    "Sally": 19,
    "Bob": 42,
    "Sue": 21,
    "Jill": 32,
    "Jack": 32,
}

```
7 - Escreva um programa em Python para calcular a soma de todos os elementos de cada tupla armazenada dentro de uma lista de tuplas.

Lista original de tuplas:

[(1, 2), (2, 3), (3, 4)]

Soma de todos os elementos de cada tupla armazenada dentro da mencionada lista de tuplas:

[3, 5, 7]

Lista original de tuplas:

[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

Soma de todos os elementos de cada tupla armazenada dentro da mencionada lista de tuplas:

[9, -1, 7, 8]

8 - Problema: Compra e Venda de Ações
Você recebe uma lista prices onde prices[i] é o preço de uma determinada ação no dia i. Você deseja maximizar seu lucro escolhendo um dia para comprar uma ação e escolhendo um dia diferente no futuro para vender essa ação. Retorne o lucro máximo que você pode obter com essa transação. Se não for possível obter lucro algum, retorne 0.


Exemplo 1:

Entrada: prices = [7,1,5,3,6,4]

Saída: 5

Explicação: Compre no dia 2 (preço = 1) e venda no dia 5 (preço = 6), lucro = 6-1 = 5. Observe que comprar no dia 2 e vender no dia 1 não é permitido, pois você deve comprar antes de vender.

Exemplo 2:

Entrada: prices = [7,6,4,3,1]

Saída: 0

Explicação: Neste caso, nenhuma transação é realizada e o lucro máximo é 0.

9 - Você recebe um número inteiro grande representado como um array de inteiros chamado 'digits', onde cada 'digits[i]' é o i-ésimo dígito do número. Os dígitos são ordenados do dígito mais significativo para o menos significativo na ordem da esquerda para a direita. O número inteiro grande não contém zeros à esquerda.

Incremente o número inteiro grande em um e retorne o array resultante de dígitos.

Exemplo 1:

Entrada: digits = [1,2,3]
Saída: [1,2,4]
Explicação: O array representa o número 123. Incrementar um resulta em 123 + 1 = 124. Portanto, o resultado deve ser [1,2,4].

Exemplo 2:

Entrada: digits = [4,3,2,1]
Saída: [4,3,2,2]
Explicação: O array representa o número 4321. Incrementar um resulta em 4321 + 1 = 4322. Portanto, o resultado deve ser [4,3,2,2].

Exemplo 3:

Entrada: digits = [9]
Saída: [1,0]
Explicação: O array representa o número 9. Incrementar um resulta em 9 + 1 = 10. Portanto, o resultado deve ser [1,0].

10 - Dado o nó inicial de uma lista ligada ordenada, exclua todos os duplicados de forma que cada elemento apareça apenas uma vez. Retorne a lista ligada também ordenada.
[Imagem](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)
