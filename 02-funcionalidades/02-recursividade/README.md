# Recursividade

## Definição


Recursão é o processo de definir algo em termos de si mesmo e é, algumas vezes, chamado de definição circular.
O conceito de algo recursivo está dentro de si, que por sua vez está dentro de si e assim sucessivamente, infinitamente

    Veja [este vídeo](https://www.youtube.com/watch?v=cHZWZhHQq4g&source_ve_path=MjM4NTE) para compreender alguns conceitos básicos sobre recusividade a partir da sequência de fibonacci.

A sequencia de fibonacci descrita no vídeo anterior é um exemplo de função recursiva. Os números presentes nesta sequencia e suas relações aparecem em diversmos momentos na natureza. 

![Tornado](https://kucdinteractive.com/croy/golden-ratio-site/assets/images/nature-img-1.jpg)

![Aloevera](http://ucanr.edu/blogs/UCMasterGardenersofSanMateoSanFranciscoC/blogfiles/102486.png)


Na computação o conceito de recursividade é amplamente utilizado, mas difere da recursividade típica por apresentar uma condição que provoca o fim do ciclo recursivo. 

A recursividade é um recurso de programação que deve ser usado com sabedoria, pois caso a condição de parada não seja bem definida o programa entrará em um loop infinito 

Em muitos casos, um problema pode ser resolvido com o uso de estrutura de repetição do tipo while ou do tipo for. 

    A recursividade é uma forma de trabalhar com problemas por meio da **divisão** do problema em partes menores quando as partes menores possuem a mesma natureza e solucioná-los (conquista) após estes passos.

## Estrutura de Funções Recursivas

Para criar uma função é recursiva devemos dividir a solução em duas etapas:
- Estabelecer a condição de parada, ou seja, o caso trivial com o qual sabemos o retorno exato.
- Existir uma chamada para a própria função com a redução do problema em problemas menores 

### Funções Matemáticas

#### Fatorial 

Fatorial é um número natural inteiro positivo, o qual é representado por **n!**. O fatorial de um número é calculado pela multiplicação desse número por todos os seus antecessores até chegar ao número 1. Note que nesses produtos, o zero (0) é excluído.

- O fatorial é representado por:
n! = n . (n – 1) . (n – 2) . (n – 3)!

- Um fatorial de um número inteiro não negativo é uma função definida como

![Fatorial](./imgs/fatorial-matematica.png)


Vejamos o exemplo de fatorial do  número 6:

    - 6!
    - 6 * 5! 
    - 6 * 5 * 4! 
    - 6 * 5 * 4 *3!
    - 6 * 5 * 4 *3 *2!
    - 6 * 5 * 4 *3 *2 *1!
    - 6 * 5 * 4 *3 *2 *1 * 0!
    - 6 * 5 * 4 *3 *2 *1 * 1

A implementação da função fatorial usando a linguagem Python pode ser da seguinte maneira utilizando estruturas de repetição:

```py
def fatorial(numero):
    if numero < 2:
        return 1

    total = 1
    for n in range(numero, -1):
        total *= n

    return total
    
```
O fatorial de um número também pode ser resolvido  recursivamente. Seguindo as regras da função, temos:
- Condição de parada: n! = 1, se n = 0
- Chamada da própria função: n! = n * (n-1)! , se n > 0

```py
def fatorial_recursivo(numero):
    if numero < 2:
        return 1
    else:
        return fatorial_recursivo(numero - 1) * numero
```

A versão não-recursiva de fatorial usa um laço que é executado de 1 a n e multiplica progressivamente cada número pelo produto. 

A versão recursiva pode ser confusa inicialmente, mas possui verbosidade menor. Quando fatorial_recursivo é chamada com um argumento menor que 2, a função devolve 1. Caso contrário, ela devolve o produto de fatorial_recursivo(n-1) * n. 

Para avaliar essa expressão, fatorial_recursivo é chamada com n-1. Isso acontece até que n se iguale a 1 e as chamadas à função comecem a retornar.

    No programa recursivo para calcular o fatorial de 6, o computador tem de calcular primeiro o fatorial de 5 e só depois é que faz a multiplicação de 6 pelo resultado. 
    
    Para calcular o fatorial de 5, vai ter de calcular o fatorial de 4 para depois multiplicar por 5. 
    
    Para calcular o fatorial de 4, vai ter que calcular o fatorial 3 para depois multiplicar por 4 e assim por diante até que tenha que calcular o fatorial de 1 quando o valor é determinado diretamente ao invés de fazer uma nova chamada recursiva. 

Ao se determinar o valor diretamente o processo de chamadas recursivas é interrompido e o valor retornado para a função recursiva que o chamou. O resultado é retornado para a função que a chamou anteriormente, repetindo o processo até que seja retornado o valor do fatorial para a primeira chamada da função.

#### Série de Fibonacci

Fibonacci (matemático da Renascença italiana) utilizou uma série curiosa de números para modelar o número de casais de coelhos em sucessivas gerações. 

    Um homem pôs um par de coelhos num lugar cercado por todos os lados por um muro. Quantos pares de coelhos podem ser gerados a partir desse par em um ano se, supostamente, todos os meses cada par dá à luz um novo par, que é fértil a partir do segundo mês?

![Fibonacci-Coelhos](./imgs/fibonacci.png)


De acordo com o problema, temos que o número de pares de coelhos em determinado mês, é a soma dos pares de coelhos existentes nos dois meses anteriores a este. Na matemática, os números de Fibonacci são os números que compõe a seguinte sucessão de números inteiros.
- 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

Em definição matemática a sequência é definida recursivamente pela fórmula abaixo:

![Função Fibonacci](./imgs/fibonacci-funcao.png)

## Funções Computacionais

A utilização de funções recursivas na computação é muito comum para problemas que lidam com dados de mesma natureza. 
– Estruturas de dados (árvores, grafos)
– Algoritmos de busca e ordenação

### Custo de funções recursivas

Quando uma função chama a si mesma, novos parâmetros e variáveis locais são alocados na pilha, sendo criado um novo contexto de execução para as variáveis e o código da função é executado com essas novas variáveis. 

Uma chamada recursiva não faz uma nova cópia da função; apenas os argumentos são novos.  Quando cada função recursiva retorna, as variáveis locais e os parâmetros são removidos da pilha e a execução recomeça do ponto da chamada à função dentro da função.









