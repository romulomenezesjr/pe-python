# Funções em Python

## Definição

Em Python, uma função é um bloco de código nomeado que pode ser chamado/executado várias vezes para realizar uma tarefa específica. As funções são uma parte fundamental da programação, pois nos permitem reutilizar código e modularizar nossa lógica. Esta é uma das principais vantagens ao criar funções, pois assim poderemos reutilizar o mesmo algoritmo/funcionalidade em outros momentos.

A definição de uma função segue a seguinte sintaxe:

```python
def nome_da_funcao(parametros):
    # Bloco de código da função
    # Pode conter várias instruções
    return valor_de_retorno
```

Você pode utilizar esta função definida por você da mesma forma que utiliza as funções embutidas no python, como print, len ou input. Vamos rever algumas características das funções embutidas para conhecer as diferentes formas de criar funções. 

## Funções Embutidas em Python

As funções embutidas em Python são recursos pré-definidos na linguagem que estão disponíveis para uso imediato, sem a necessidade de importações ou definições adicionais. Elas fornecem funcionalidades comuns e importantes para o desenvolvimento de programas Python. Vamos explorar algumas das funções embutidas mais utilizadas:

Algumas funções comuns são `print()`, `len()`, `input()`, `range()`, `sum()`, `max()`, `min()`, entre outras.

### `print()`

A função `print()` é amplamente utilizada para exibir informações na saída padrão (normalmente no console). Ela pode receber um ou mais argumentos separados por vírgulas e imprime-os na ordem fornecida.

Exemplo:

```python
print("Olá, mundo!")
```

### `len()`

A função `len()` retorna o tamanho (número de elementos) de uma sequência, como uma string, lista, tupla, etc.

Exemplo:

```python
texto = "Python"
print(len(texto))  # Saída: 6
```

### `input()`

A função `input()` é usada para receber entrada do usuário. Ela exibe uma mensagem (prompt) ao usuário, espera que o usuário digite algo e retorna a entrada como uma string.

Exemplo:

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

### `range()`

A função `range()` é usada para criar sequências de números. Pode ser utilizada de diversas formas, mas a mais comum é com apenas um argumento, que representa o valor final da sequência (o valor inicial é assumido como 0).

Exemplo:

```python
for i in range(5):
    print(i)  # Saída: 0, 1, 2, 3, 4
```

### `sum()`, `max()` e `min()`

Essas funções são usadas para calcular a soma, o valor máximo e o valor mínimo de uma sequência de números, respectivamente.

Exemplo:

```python
numeros = [1, 5, 3, 8, 2]
print(sum(numeros))  # Saída: 19
print(max(numeros))  # Saída: 8
print(min(numeros))  # Saída: 1
```

### `sorted()`

A função `sorted()` é usada para ordenar os elementos de uma sequência, retornando uma nova lista com os elementos ordenados.

Exemplo:

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
```

Essas são apenas algumas das muitas funções embutidas disponíveis em Python. Conhecê-las e utilizá-las apropriadamente pode facilitar muito o desenvolvimento de programas Python eficientes e funcionais. Além de conhecer as funções embutidas você deve construir suas próprias funções que possuam comportamento útil para utilizar nos programas. Programar é basicamente criar e utilizar funções que possam ser utilizadas ao longo da execução de acordo com o algoritmo pré-estabelecido. 

## Parâmetros, parâmetros nomeados, retornos

As funções podem receber parâmetros, que são valores que a função utiliza para realizar suas tarefas. Os parâmetros são especificados entre os parênteses na definição da função. É possível usar parâmetros nomeados, onde o nome do parâmetro é especificado ao chamar a função. Além disso, as funções podem retornar um valor utilizando a palavra-chave `return`.

### Parâmetros em Funções

Os parâmetros em funções são variáveis que permitem que você passe valores para dentro da função quando ela é chamada. Esses valores são utilizados dentro do bloco de código da função para realizar suas operações. As funções podem receber um ou mais parâmetros, e eles são definidos na declaração da função entre os parênteses.

Exemplo de função com parâmetros:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Neste exemplo, a função `saudacao` recebe um parâmetro chamado `nome`, que é utilizado para exibir uma mensagem personalizada na saudação.

Uma função pode ser criada com mais de um parâmetro para permitir que diversos dados sejam  manipulados.  Podemos definir uma função saudacao recebendo nome e sexo para que a função imprima o pronome de tratamento correto.


```python
def saudacao(nome, sexo):
    if sexo == 'f':
        print(f"Olá, senhora {nome}!")
    elif sexo == 'm':
        print(f"Olá, senhor {nome}!")        
    else:
        print(f"Olá, {nome}!")

saudacao('José', 'm')
```

Observe que a ordem de passagem dos parâmetros deve ser seguida para que as variáveis da função sejam manipuladas na ordem correta. Tente executar a função saudação invertendo os parâmetros.


### Parâmetros Nomeados

Em Python, é possível chamar uma função especificando o nome dos parâmetros e seus respectivos valores. Isso é conhecido como parâmetros nomeados (ou argumentos nomeados). Dessa forma, a ordem dos parâmetros não importa, pois a função identifica os valores corretos pelos seus nomes.

Exemplo de função com parâmetros nomeados:

```python
def saudacao(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}!")
```

Chamada da função com parâmetros nomeados:

```python
saudacao(sobrenome="Silva", nome="João")
```

### Retornos em Funções

As funções podem retornar um valor de volta para quem as chamou utilizando a palavra-chave `return`. O valor retornado pode ser armazenado em uma variável ou usado em outras operações.

Exemplo de função com retorno:

```python
def soma(a, b):
    resultado = a + b
    return resultado
```

Chamada da função com retorno:

```python
resultado_soma = soma(3, 5)
print(resultado_soma)  # Saída: 8
```

É importante notar que a presença da instrução `return` finaliza a execução da função e retorna o valor indicado. Caso a função não possua um `return`, ela retorna implicitamente `None`.

Exemplo de função sem retorno explícito:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
    # Sem instrução return

resultado = saudacao("Maria")
print(resultado)  # Saída: None
```

## Tipagem Opcional

Em Python, as funções não têm uma tipagem rígida para parâmetros e retornos. Isso significa que você pode passar argumentos de tipos diferentes para a função sem necessidade de definir os tipos dos parâmetros na declaração da função. Isso é conhecido como tipagem opcional.

Exemplo de função com tipagem opcional:

```python
def soma(a, b):
    resultado = a + b
    return resultado
```

Chamada da função com tipos diferentes:

```python
resultado_soma1 = soma(3, 5)
resultado_soma2 = soma("Olá, ", "Mundo!")
print(resultado_soma1)  # Saída: 8
print(resultado_soma2)  # Saída: Olá, Mundo!
```

A tipagem opcional é uma característica importante do Python, pois torna a linguagem mais flexível e facilita a escrita de código.

Essas são algumas das principais informações sobre parâmetros, parâmetros nomeados e retornos em funções em Python. Com esses conceitos, você poderá criar funções mais flexíveis e úteis para suas necessidades.

Em Python, é possível fazer uso de declaração de tipos em funções, parâmetros e retornos através das "Annotations" (anotações). As anotações não são obrigatórias, mas permitem especificar os tipos esperados de parâmetros e o tipo de retorno da função. Essa prática é conhecida como "Type Hinting" ou "Duck Typing".

A declaração de tipos não afeta o comportamento em tempo de execução da função, ou seja, não causa erros ou verificações em tempo de execução. No entanto, as anotações podem ser úteis para melhorar a legibilidade do código, facilitar a colaboração entre membros da equipe e ajudar em ferramentas de análise de código.

### Declaração de Tipos em Parâmetros

Para declarar o tipo esperado de um parâmetro em uma função, basta colocar o nome do parâmetro seguido de `:` e o tipo desejado após ele.

Exemplo:

```python
def soma(a: int, b: int) -> int:
    resultado = a + b
    return resultado
```

Neste exemplo, a função `soma` possui dois parâmetros `a` e `b`, ambos do tipo `int`, e o tipo de retorno da função é declarado como `int`.

### Declaração de Tipo de Retorno

Para especificar o tipo de retorno da função, utiliza-se a seta `->` seguida do tipo desejado após o `:`.

Exemplo:

```python
def saudacao(nome: str) -> str:
    return "Olá, " + nome
```

A função `saudacao` recebe um parâmetro `nome` do tipo `str` e retorna uma saudação, que também é do tipo `str`.

### Declaração de Tipo Opcional

As declarações de tipo são opcionais em Python, mas podem ser úteis para fins de documentação e verificação de tipo em ferramentas de análise de código (como o Mypy). Caso as declarações de tipo não sejam fornecidas, o interpretador Python ainda funcionará normalmente.

Exemplo sem declarações de tipo:

```python
def multiplicacao(a, b):
    return a * b
```

Exemplo com declarações de tipo:

```python
def multiplicacao(a: int, b: int) -> int:
    return a * b
```

### Tipos Compostos e Anotações Avançadas

Além de tipos simples, também é possível usar tipos compostos como listas, dicionários e tuplas, bem como tipos personalizados definidos pelo usuário. Para tipos compostos, utilize colchetes `[]` para listas, chaves `{}` para dicionários e parênteses `()` para tuplas.

Exemplo com tipos compostos:

```python
from typing import List, Dict, Tuple

def processa_dados(dados: List[str]) -> Dict[str, int]:
    resultado: Dict[str, int] = {}
    for item in dados:
        resultado[item] = len(item)
    return resultado
```

Neste exemplo, a função `processa_dados` recebe uma lista de strings e retorna um dicionário com as strings e seus respectivos tamanhos.

### Nota sobre Verificação de Tipo

Apesar de permitir a declaração de tipos, o Python não realiza verificações de tipo em tempo de execução por padrão. As declarações de tipo são destinadas principalmente para fins de documentação e auxílio em ferramentas de análise de código. Se você deseja adicionar verificações de tipo, pode usar ferramentas como o Mypy.

Em resumo, a declaração de tipos em funções, parâmetros e retornos é uma prática opcional e flexível em Python que pode melhorar a legibilidade e a documentação do código, além de facilitar a colaboração entre desenvolvedores e auxiliar em ferramentas de análise de código.

## Escopo Local e Escopo Global em Python#

Em Python, o conceito de escopo refere-se à visibilidade e acessibilidade de variáveis em diferentes partes do código. Existem dois principais escopos em Python: escopo local e escopo global.

### 1. Escopo Local:

- O escopo local refere-se às variáveis que são definidas dentro de uma função.
- Essas variáveis só são acessíveis dentro da função em que foram criadas.
- Quando a função termina de ser executada, as variáveis locais deixam de existir.
- Se tentarmos acessar uma variável local fora da função, ocorrerá um erro de "NameError".

Exemplo de escopo local:

```python
def minha_funcao():
    x = 10  # Variável local, só visível dentro da função
    print(x)

minha_funcao()  # Saída: 10
print(x)  # Erro: NameError: name 'x' is not defined
```

### 2. Escopo Global:

- O escopo global refere-se às variáveis que são definidas fora de qualquer função ou bloco de código.
- Essas variáveis são acessíveis em todo o programa, em qualquer função.
- Variáveis globais podem ser lidas (usadas) em uma função sem a necessidade de declará-las novamente, mas para modificá-las, é preciso usar a palavra-chave "global" para informar ao Python que queremos modificar a variável global e não criar uma variável local com o mesmo nome.

Exemplo de escopo global:

```python
x = 10  # Variável global

def minha_funcao():
    print(x)  # Variável global acessível dentro da função

minha_funcao()  # Saída: 10

def altera_variavel_global():
    global x
    x = 20  # Modificando a variável global
    print(x)

altera_variavel_global()  # Saída: 20
print(x)  # Saída: 20 (variável global foi modificada)
```

### Observações:

- É importante usar variáveis globais com cautela, pois o acesso global pode tornar o código menos legível e mais difícil de depurar.
- Em geral, é recomendado usar variáveis locais sempre que possível e passar os valores necessários como argumentos para as funções em vez de depender de variáveis globais.

## Encadeamento de Escopos (Closure):

Python também permite a criação de funções dentro de funções, o que gera uma estrutura de escopos encadeados. Nesse caso, a função interna (função aninhada) tem acesso ao escopo local da função externa (função pai).

Exemplo de encadeamento de escopos:

```python
def funcao_pai():
    x = 10

    def funcao_filha():
        print(x)  # A função filha pode acessar a variável x da função pai

    funcao_filha()

funcao_pai()  # Saída: 10
```

Compreender o escopo local e global em Python é fundamental para escrever código limpo, modular e eficiente, pois permite que você trabalhe com variáveis de maneira organizada e controlada. É importante ter cuidado ao utilizar variáveis globais, pois o uso excessivo pode dificultar a manutenção do código e causar efeitos colaterais indesejados.

Variáveis definidas dentro de uma função têm escopo local, o que significa que elas só podem ser acessadas dentro dessa função. Variáveis definidas fora de qualquer função têm escopo global e podem ser acessadas em qualquer lugar do código.

## Argumentos \*args e \*\*kwargs

Python permite definir funções que aceitam um número variável de argumentos através das notações `*args` e `**kwargs`. O `*args` permite passar múltiplos argumentos posicionais como uma tupla, e o `**kwargs` permite passar múltiplos argumentos nomeados como um dicionário. Essas duas notações especiais permitem que você escreva funções flexíveis que podem receber um número indefinido de argumentos, tornando-as mais versáteis e poderosas.

### `*args`

O `*args` é usado para passar um número arbitrário de argumentos posicionais para uma função. O `*` antes de `args` indica que os argumentos serão empacotados em uma tupla, que pode ser acessada dentro da função.

Exemplo:

```python
def soma(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = soma(1, 2, 3, 4, 5)
print(resultado)  # Saída: 15
```

Neste exemplo, a função `soma` recebeu um número variável de argumentos e somou todos eles.

### `**kwargs`

O `**kwargs` é usado para passar um número arbitrário de argumentos nomeados (keyword arguments) para uma função. O `**` antes de `kwargs` indica que os argumentos nomeados serão empacotados em um dicionário, que pode ser acessado dentro da função.

Exemplo:

```python
def saudacao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

saudacao(nome="Alice", idade=25, cidade="São Paulo")
```

Neste exemplo, a função `saudacao` recebeu argumentos nomeados e os exibiu em formato de chave-valor.

### Utilizando ambos `*args` e `**kwargs`

Você pode utilizar `*args` e `**kwargs` juntos em uma mesma função, permitindo que ela aceite qualquer combinação de argumentos posicionais e nomeados.

Exemplo:

```python
def exemplo(*args, **kwargs):
    print("Argumentos posicionais:")
    for arg in args:
        print(arg)

    print("\nArgumentos nomeados:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exemplo(1, 2, 3, nome="Alice", idade=25)
```

Neste exemplo, a função `exemplo` recebeu argumentos posicionais e argumentos nomeados, exibindo ambos.

### Importante:

- O uso de `*args` e `**kwargs` é opcional e eles podem receber qualquer nome válido, mas a convenção é utilizar esses nomes para maior clareza.
- A ordem dos parâmetros na declaração da função é importante. A sequência geralmente é `parâmetros`, `*args`, `**kwargs`.
- O uso adequado de `*args` e `**kwargs` torna suas funções mais flexíveis e permite que elas lidem com diferentes cenários sem a necessidade de definir vários parâmetros fixos.
- No entanto, lembre-se de que a legibilidade do código é importante, então use essas notações com parcimônia e de forma adequada aos requisitos da sua aplicação.

## Documentação de Código e Documentação de Funções em Python

A documentação em Python é uma prática importante para tornar o código mais legível, facilitar a manutenção e colaboração entre desenvolvedores. A documentação pode ser feita de diferentes formas, incluindo comentários explicativos no código e docstrings (strings de documentação) para descrever funções, módulos e classes.

### Comentários

Comentários são trechos de texto que explicam o funcionamento do código. Eles são precedidos pelo caractere `#` e são ignorados pelo interpretador Python, ou seja, não afetam a execução do programa. Comentários são úteis para adicionar notas explicativas, esclarecimentos e dicas para outras pessoas (incluindo você mesmo no futuro) que lerão o código.

Exemplo de comentário:

```python
# Calcula a média de uma lista de números
def calcular_media(lista):
    total = sum(lista)
    media = total / len(lista)
    return media
```

### Docstrings (Strings de Documentação)

As docstrings são strings que descrevem o propósito e o comportamento de funções, módulos ou classes em Python. Elas são colocadas logo após a definição de uma função, módulo ou classe, entre três aspas (simples ou duplas) e permitem que você escreva uma descrição mais detalhada da funcionalidade.

Exemplo de docstring em uma função:

```python
def calcular_media(lista):
    """
    Calcula a média de uma lista de números.

    Parâmetros:
    lista (list): Uma lista contendo números para calcular a média.

    Retorna:
    float: A média dos números na lista.
    """
    total = sum(lista)
    media = total / len(lista)
    return media
```

As docstrings são acessíveis usando a função `help()` ou como atributo especial `__doc__`. Elas são extremamente úteis para outros desenvolvedores entenderem o propósito e uso de funções, especialmente em módulos compartilhados ou em bibliotecas.

Exemplo de uso da docstring com a função `help()`:

```python
help(calcular_media)
```

### PEP 257

A PEP (Python Enhancement Proposal) 257 fornece diretrizes para escrever docstrings de forma consistente e padronizada. Seguir as diretrizes da PEP 257 ajuda a garantir que a documentação seja clara e facilite a leitura e compreensão do código.

Exemplo de docstring seguindo as diretrizes da PEP 257:

```python
def calcular_media(lista):
    """
    Retorna a média de uma lista de números.

    :param lista: Uma lista contendo números para calcular a média.
    :type lista: list
    :return: A média dos números na lista.
    :rtype: float
    """
    total = sum(lista)
    media = total / len(lista)
    return media
```

Documentar adequadamente seu código, seja com comentários explicativos ou docstrings detalhadas, é uma prática essencial para tornar seu código mais legível e colaborativo. Isso também ajudará outros desenvolvedores a compreender rapidamente suas intenções e facilitará a manutenção do código ao longo do tempo.

## High Order Functions (HOF) e First Class Functions em Python

Python suporta High Order Functions (HOF), o que significa que as funções podem ser passadas como argumentos para outras funções ou retornadas por elas. Além disso, Python trata as funções como objetos de primeira classe (First Class Functions), o que permite atribuí-las a variáveis, armazená-las em estruturas de dados e passá-las como parâmetros.

### First Class Functions

Em Python, as funções são consideradas "First Class Functions", o que significa que elas são tratadas como cidadãos de primeira classe. Isso possibilita que as funções sejam tratadas da mesma forma que outros tipos de dados, como inteiros, strings e listas. Algumas características das First Class Functions em Python são:

1. As funções podem ser atribuídas a variáveis:

   ```python
   def saudacao(nome):
       return f"Olá, {nome}!"

   mensagem = saudacao
   print(mensagem("João"))  # Saída: "Olá, João!"
   ```

2. As funções podem ser passadas como argumentos para outras funções:

   ```python
   def somar(a, b):
       return a + b

   def operacao_matematica(funcao, x, y):
       return funcao(x, y)

   resultado = operacao_matematica(somar, 3, 5)
   print(resultado)  # Saída: 8
   ```

3. As funções podem ser retornadas por outras funções:

   ```python
   def criar_funcao(op):
       if op == "soma":
           def soma(a, b):
               return a + b
           return soma
       elif op == "subtracao":
           def subtracao(a, b):
               return a - b
           return subtracao

   operacao = criar_funcao("soma")
   resultado = operacao(3, 5)
   print(resultado)  # Saída: 8
   ```

### High Order Functions (HOF)

Uma "High Order Function" (HOF) é uma função que aceita outras funções como argumentos e/ou retorna funções. Em outras palavras, as HOFs manipulam funções e as utilizam como parte de sua lógica. As HOFs são uma parte importante da programação funcional em Python.

Um exemplo de HOF é a função `map()`, que recebe uma função e um iterável como argumentos e aplica essa função a cada elemento do iterável, retornando um novo iterável com os resultados.

Exemplo de uso da função `map()`:

```python
def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
dobro = map(dobrar, numeros)
print(list(dobro))  # Saída: [2, 4, 6, 8, 10]
```

Outro exemplo é a função `filter()`, que filtra os elementos de um iterável com base em uma função de teste.

Exemplo de uso da função `filter()`:

```python
def e_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5]
pares = filter(e_par, numeros)
print(list(pares))  # Saída: [2, 4]
```

As High Order Functions proporcionam maior flexibilidade e poder à programação em Python, permitindo que as funções sejam tratadas como dados e aplicadas a diferentes cenários de maneira mais elegante e concisa. Elas são amplamente utilizadas em programação funcional, facilitando a criação de código mais modular e de fácil manutenção.

## Funções Lambda em Python

As funções lambda em Python são funções anônimas e pequenas que podem ser definidas em uma única linha. Elas são uma forma concisa e rápida de criar funções simples que são usadas apenas uma vez e não precisam de um nome explícito.

### Sintaxe

A sintaxe para criar uma função lambda é a seguinte:

```python
lambda argumentos: expressao
```

- `lambda`: Palavra-chave que indica que estamos criando uma função lambda.
- `argumentos`: Parâmetros da função, separados por vírgula.
- `expressao`: Expressão que define o retorno da função.

### Exemplos

Exemplo de uma função lambda que retorna o dobro de um número:

```python
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
```

Exemplo de uma função lambda que retorna a soma de dois números:

```python
soma = lambda a, b: a + b
print(soma(3, 7))  # Saída: 10
```

### Utilização de Lambdas com Funções HOF

As funções lambda são frequentemente usadas com funções HOF (High Order Functions), como `map()`, `filter()` e `sorted()`, que aceitam funções como argumentos.

Exemplo usando `map()` com lambda:

```python
numeros = [1, 2, 3, 4, 5]
dobro = map(lambda x: x * 2, numeros)
print(list(dobro))  # Saída: [2, 4, 6, 8, 10]
```

Exemplo usando `filter()` com lambda:

```python
numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4]
```

### Limitações das Funções Lambda

As funções lambda são úteis para tarefas simples e pontuais, mas têm algumas limitações:

1. Podem conter apenas uma expressão, portanto, não suportam múltiplas linhas de código.
2. Não podem conter declarações ou comandos complexos, como loops ou condicionais.

Devido a essas limitações, as funções lambda são mais indicadas para situações em que uma função pequena e rápida é necessária, como uma função de transformação para uma função HOF.

Em resumo, as funções lambda são uma ferramenta útil para criar funções anônimas e pequenas em Python. Elas são frequentemente utilizadas com funções HOF para simplificar o código e torná-lo mais conciso. No entanto, para funções mais complexas, é recomendado o uso de funções nomeadas tradicionais.
