# Parte 1
Q01: Escreva um programa que imprima todos os números pares de 0 a 50 utilizando um loop "for".

Q02: Escreva um programa que peça ao usuário para digitar um número e, em seguida, imprima a tabuada desse número (de 1 a 10) utilizando um loop "for".

Q03: Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, imprima cada letra da palavra em uma linha separada utilizando um loop "for".

Q04: Escreva um programa que utilize um loop "for" para calcular a soma de todos os números ímpares de 1 a 100.

Q05:Escreva um programa que peça ao usuário para digitar uma frase e, em seguida, conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".

Q06: Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, imprima a palavra ao contrário utilizando um loop "for".

Q07:Escreva um programa que utilize um loop "while" para imprimir os números de 1 a 10.

Q08: Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. O programa deve informar se o palpite é muito alto, muito baixo ou correto. Continue pedindo ao usuário para adivinhar até que ele acerte o número utilizando um loop "while".

Q09: Escreva um programa que peça ao usuário para digitar uma série de números (um por linha) e pare quando o usuário digitar um número negativo. Em seguida, calcule e imprima a média dos números digitados.

Q10: Escreva um programa que peça ao usuário para digitar uma senha e continue pedindo até que o usuário digite a senha correta. Quando a senha estiver correta, imprima uma mensagem de boas-vindas.

Q11: Escreva um programa que utilize um loop "for" e a função range() para imprimir todos os números pares de 0 a 20.

Q12: Dada a lista de frutas e a lista de cores abaixo, utilize a função zip() e um loop "for" para imprimir cada fruta com sua respectiva cor.

```python
frutas = ['maçã', 'banana', 'laranja', 'uva']
cores = ['vermelho', 'amarelo', 'laranja', 'roxa']

```

Q13: Utilize a função enumerate() e um loop "for" para imprimir os elementos das listas da questão anterior, juntamente com seus índices.

Q14: Escreva um programa que utilize um loop "for" e a função reversed() para imprimir os números de 10 a 1 em ordem decrescente.

Q15: Dada a lista de números abaixo, utilize a função sorted() e um loop "for" para imprimir os números em ordem crescente.

# Parte 2

Q16: Escreva  um  programa  que  imprime  na  tela  os  n  primeiros  números  perfeitos.  Um  número  perfeito  é  aquele  que  é  igual  à  soma  dos  seus  divisores. Por exemplo, 6 = 1 + 2 + 3. 

Q17: Um  número inteiro  é  considerado  triangular  se  este  for  o  produto  de  3  números  inteiros  consecutivos,  como,  por  exemplo,  120  =  4  x  5  x  6.  Elabore um programa que, após ler um número n do teclado, verifique se  n é triangular. 

Q18: Elabore  um  programa  que  leia  n  valores  e  mostre  a  soma  de  seus  quadrados. 

Q19: Faça  um  programa  que  leia  dois  valores  x  e  y,  e  calcula  o  valor  de  x  dividido  por  y,  além  do  resto  da  divisão.  Não  é  permitido  usar  as  operações  de  divisão  e  resto  de  divisão  do  Python  (use  apenas  soma  e  subtração)

Q20:  Faça  um  programa  que  calcule  o  número  de  dias  corridos  entre  duas  datas,  para  vários  pares  de  datas,  considerando  a  possibilidade  de  ocorrência de anos bissextos, sendo que:  
- A primeira data é sempre a mais antiga 
- O ano é fornecido com 4 dígitos 
- A data  fornecida com ZERO dias é o sinal para encerrar a entrada  de dados

Q21: Foi realizada uma pesquisa em Niterói, com um número desconhecido de  pessoas. De cada entrevistado foram colhidos os seguintes dados:  

  1. Qual  o  seu  clube  de  futebol  de  preferência  (1  – Flamengo,  2  –   Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros) 
  2. Qual o seu salário 
  3. Qual a sua cidade natal (1 – Niterói, 2 – Outra)
     
Escreva um programa que informe: 
- Número de torcedores por clube 
- Média salarial dos torcedores de cada time 
- Número  de  pessoas  nascidas  em  Niterói  e  que  não  torcem  para  nenhum dos principais clubes do Rio 
- Número de pessoas entrevistadas

Q22: Faça  um  programa  em  Python  que  calcule  o  valor  de  Pi,  utilizando  a  fórmula de Leibniz: π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 + ...
Adicione parcelas no cálculo até que a diferença de uma interação para a  seguinte seja menor do que um valor de erro aceitável x informado pelo  usuário. 

Q23:  Numa lanchonete, uma pessoa pode comprar Nuggets apenas em pacotes  contendo 6, 9 ou 20 pedaços. Escreva um programa em Python que lê um valor  inteiro  num e  que  imprima  True se  é  possível  comprar  num Nuggets nessa lanchonete, ou Falso, caso contrário. Por exemplo, se num  = 44, o programa deve retornar True (seria um pacote de 6, dois de 9 e 1  um  de  20,  por  exemplo).  Mas  se  num  =  34,  o  programa  deve  retornar  False

Q24: O quadrado de um numero natural n é dado pela soma dos n primeiros  números  impares  consecutivos.  Por  exemplo,  1^2=1,  2^2=1+3,  3^2=1+3+5,  4^2=1+3+5+7, etc.  Escreva  um  programa  que  dado  um  número n,  calcule  seu quadrado usando a soma de ímpares ao invés de produto.

Q25: Generalize o exercício anterior, de forma que ele calcule e mostre na tela  os quadrados de todos os números naturais menores que 1000, usando o  método da soma de ímpares. 

Q26:  Faça  um  programa  que  simula  uma  calculadora  que  aceita  as  seguintes  operações:  soma,  subtração,  divisão  e  multiplicação.  O  programa  inicia  pedindo para o usuário escolher uma opção do menu 
1. Somar 
2. Subtrair 
3. Dividir 
4. Multiplicar 
5. Sair  
Ao  escolher  a  opção,  o  programa  solicita  os  dois  números  a  serem  operados (exceto se a opção escolhida for a 5), efetua a operação, mostra  o resultado na tela e volta para o menu para que o usuário escolha outra  opção. 

