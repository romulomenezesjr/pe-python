# Instrução de seleção simples (if):

A instrução "if" é usada para executar um bloco de código se uma condição for avaliada como verdadeira. A sintaxe básica é a seguinte:

```python
if condição:
    # código a ser executado se a condição for verdadeira

```

Se a condição for verdadeira, o código dentro do bloco de "if" será executado. Caso contrário, o bloco será ignorado e a execução continuará com o próximo bloco de código.

```python
idade = 18
if idade >= 18:
    print("Você pode votar.")

```

O if avalia um valor booleano, logo este valor pode sugir de uma expressão lógica ou relacional. Veja o exemplo a seguir com o operador lógico **and**:

```python
idade = 25
tem_carteira_de_motorista = True

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

```

Veja o exemplo utilizando o operador relacional **==**

```python
senha_correta = "12345"
senha_digitada = input("Digite sua senha: ")

if senha_digitada == senha_correta:
    print("Acesso concedido.")
else:
    print("Senha incorreta. Acesso negado.")

```

Veja o exemplo utilizando o operador de associação **in**

```python
cores_preferidas = ["azul", "vermelho", "verde"]
cor_escolhida = input("Digite sua cor preferida: ")

if cor_escolhida in cores_preferidas:
    print("Essa cor está na lista das suas cores preferidas.")
else:
    print("Essa cor não está na lista das suas cores preferidas.")

```

# Instrução de seleção dupla (if/else):

A instrução "if/else" permite executar um bloco de código quando uma condição é verdadeira e outro bloco de código quando a condição é falsa. A sintaxe é a seguinte:

```python
if condição:
    # código a ser executado se a condição for verdadeira
else:
    # código a ser executado se a condição for falsa

```

Exemplo:

```python
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

```

# Instruções if/else aninhadas

As instruções if/else aninhadas permitem criar estruturas de decisão mais complexas, em que condições adicionais são testadas dentro dos blocos de código associados aos comandos if e else. Isso é útil quando você precisa verificar múltiplas condições em sequência para determinar o fluxo do programa.

Aqui está a estrutura geral de instruções if/else aninhadas em Python:

```python
if condição_1:
    # código a ser executado se a condição_1 for verdadeira
else:
    if condição_2:
        # código a ser executado se a condição_1 for falsa e condição_2 for verdadeira
    else:
        # código a ser executado se a condição_1 e a condição_2 forem falsas

```

Você pode adicionar mais blocos "else" aninhados para testar condições adicionais. Os blocos serão executados sequencialmente, de cima para baixo, até que uma condição seja verdadeira ou até que todos os blocos tenham sido verificados.

Vamos ver um exemplo para melhor entender:

```python
idade = 25
tem_carteira_de_motorista = True
tem_passagem_aerea = False

if idade >= 18:
    if tem_carteira_de_motorista:
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir sem carteira de motorista.")
else:
    if tem_passagem_aerea:
        print("Sua viagem está confirmada.")
    else:
        print("Você não pode viajar sem ser maior de idade ou sem passagem aérea.")

```

As instruções if/else aninhadas podem se tornar mais complexas à medida que você adiciona mais condições, mas são muito úteis para implementar lógica condicional mais elaborada em seus programas. Lembre-se de manter a estrutura de indentação correta para evitar erros de sintaxe em Python.

Você pode substituir as estruturas aninhadas com operadores booleanos. Faça isso no exemplo anterior.

# Instrução de seleção múltipla (if/else/elif):

A instrução "if/else/elif" é usada para testar várias condições em sequência. A palavra-chave "elif" é uma abreviação de "else if" e permite verificar condições adicionais após o primeiro "if". A sintaxe é a seguinte:

```python
if condição1:
    # código a ser executado se a condição1 for verdadeira
elif condição2:
    # código a ser executado se a condição2 for verdadeira
elif condição3:
    # código a ser executado se a condição3 for verdadeira
else:
    # código a ser executado se nenhuma das condições anteriores for verdadeira

```

Exemplo

```python
nota = 75
if nota >= 90:
    print("Aprovado com nota A.")
elif nota >= 80:
    print("Aprovado com nota B.")
elif nota >= 70:
    print("Aprovado com nota C.")
else:
    print("Reprovado.")

```

# Operador ternário:

O operador ternário é uma forma concisa de escrever uma instrução de seleção simples. Ele permite avaliar uma condição e retornar um valor com base no resultado da condição, tudo em uma única linha. A sintaxe é a seguinte:

```python
valor_se_verdadeiro if condição else valor_se_falso

```

Exemplo:

```python
idade = 20
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)

```

Neste exemplo, a variável "mensagem" receberá o valor "Maior de idade" se a idade for maior ou igual a 18, caso contrário, receberá o valor "Menor de idade".

# Match Case

O match case é uma estrutura de controle introduzida na versão Python 3.10 que permite fazer correspondência de padrões (pattern matching) em valores de uma forma mais concisa e expressiva. Ele é projetado para substituir o uso de múltiplas declarações if/elif/else ou ações complexas com o operador ternário.

O match case é particularmente útil quando você precisa verificar o valor de uma variável em várias condições diferentes e deseja executar ações específicas com base no padrão correspondente. Vamos ver como funciona:

Sintaxe:

```python
match valor:
    case padrão1:
        # Ação para o padrão1
    case padrão2:
        # Ação para o padrão2
    case padrão3 if condição:
        # Ação para o padrão3 com condição extra
    case _:
        # Ação padrão (opcional) quando nenhum dos padrões anteriores corresponde

```

Aqui estão alguns exemplos para ajudar a entender melhor:

Exemplo 1 - Correspondência exata:

```python
def verificar_tipo(dado):
    match dado:
        case int:
            print("É um número inteiro.")
        case float:
            print("É um número de ponto flutuante.")
        case str:
            print("É uma string.")
        case _:
            print("Tipo não reconhecido.")

verificar_tipo(10)         # Saída: É um número inteiro.
verificar_tipo(3.14)       # Saída: É um número de ponto flutuante.
verificar_tipo("Python")   # Saída: É uma string.
verificar_tipo(True)       # Saída: Tipo não reconhecido.

```

Exemplo 2 - Correspondência com condição:

```python
def classificar_valor(valor):
    match valor:
        case x if x < 0:
            print("Valor negativo")
        case 0:
            print("Valor igual a zero")
        case x if x > 0:
            print("Valor positivo")
        case _:
            print("Valor não reconhecido")

classificar_valor(-5)    # Saída: Valor negativo
classificar_valor(0)     # Saída: Valor igual a zero
classificar_valor(10)    # Saída: Valor positivo
classificar_valor("abc") # Saída: Valor não reconhecido

```

Lembre-se de que, para usar o match case, você precisa ter Python 3.10 ou uma versão posterior instalada em seu ambiente. Se você estiver usando uma versão anterior, o match case não estará disponível, e você precisará utilizar outras estruturas condicionais, como if/elif/else, para realizar as mesmas tarefas.

Veremos a frente como utilizar dicionários para substituir if/else em algumas situações específicas. Essa técnica é útil quando você tem um conjunto de valores de entrada e suas correspondentes saídas e deseja evitar várias declarações if/else.
