# Funções de Input/Output

No Python, as funções de input e output são usadas para interagir com o usuário e com o ambiente externo. Elas permitem que você receba dados de entrada (input) e exiba informações de saída (output).

## Input

A função input() recebe uma string que será impressa na linha de comando e é capaz de ler do teclado as informações digitadas pelo usuário da seguinte forma:

```sh
# Interpretador Python no Shell
>>> valor_lido = input("Digite um valor: ")
digite um valor: 10

>>> type(valor_lido)  # O valor lido é SEMPRE do tipo string
<class 'str'>
```

O valor retornado pela função é sempre do tipo string. Para transformar o valor lido de str para outros tipos é necessário converter. Para converter para int ou float pode-se usar as funções int() e float(), que convertem o valor lido para o tipo de dado esperado.

```sh
>>> valor_lido = int(input("digite um valor inteiro: "))
digite um valor inteiro: 10

>>> type(valor_lido)
<class 'int'>

>>> valor_lido + 10
20

>>> valor_lido = float(input("digite um valor decimal: "))
digite um valor decimal: 1.5

>>> valor_lido - 1
0.5

```

Após a conversão é possível realizar as operações aritméticas com números. Caso não fizermos a conversão o que ocorreria com o resultado?

## Output

A função de print() é usada para exibir informações para o usuário ou gravá-las em um arquivo ou em outro dispositivo de saída. Aqui está um exemplo simples de uso da função print():

```python
nome = "João"
idade = 25
print("O nome é", nome, "e a idade é", idade)

```

## Conhecendo mais funções

Uma função é basicamente uma caixa preta de código, que recebeu um nome específico. De forma geral, são passados dados (parâmetros) para os argumentos de uma função que executa algumas instruções e então retorna algum valor.

### Argumentos e Retorno

No exemplo a seguir utilizamos a função print passando um argumento à ela, uma string 'Hello world!'. Ao longo de seu funcionamento a função imprime na tela o que foi fornecido a ela. Esta função não possui nenhum retorno (na verdade retorna um tipo None)

```python
dado = print('hello word')
# hello word
dado
type(dado)
# <class 'NoneType'>
```

Uma função pode ou ter receber argumentos. Para executar uma função é necessario, após o nome de uma função, colocar parênteses. Caso não coloquemos paranteses a função pode ser considerada como um tipo de dado.

```python
# Interpretador Python
type(print)
# <class 'builtin_function_or_method'>
```

Caso a função não tenha argumentos, não haverá nada dentro dos parênteses. Algumas funções aceitam mais de um argumento, e esses devem ser separados por vírgulas.

### Conhecendo a função melhor

Podemos conhecer o funcionamento de funções a partir da documentação. Desta forma conhecemos o que ela faz, os argumentos e retorno.

Também podemos visualizar isto pelos recursos da IDE/Editor de código colocando o cursos do mouse em cima do texto da função ou pela função help() do Python. Veja o exemplo:

![VS Code](../img/print-help.png)

```python
help(print)
Help on built-in function print in module builtins:
"""
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
"""
```

Para a função print o primeiro parâmetro é o valor a ser impresso. Os demais não são obrigatórios. Executando a função print com e sem parâmetros.

```python
print("Hello world!")
print()
print('Hello world!')
```

Executando a função print com um arquivo para que a saída não vá direto para a saída padrão do sistema (terminal de texto). Observe que o parâmetro file foi passado explicitamente. Caso contrário a sequência de valores deveria ser seguida (valor, separador, final, arquivo).

```python
f = open('file.txt','w')
print("hello word",file=f)
```

Agora, note que foram fornecidos dois argumentos, separados por vírgula. O que o comando print fez foi juntá-los com um espaço e colocar na mesma linha. O segundo parâmetro foi recebido como separador.

```python
print("hello word","!")
# hello word !
```

Uma outra forma mais segura para abrir, escrever e fechar o arquivo é com o uso do operador 'with'. Veja no exemplo a seguir:

```python
with open('file.txt','w') as f:
    print("hello word",file=f)
```
Exercício: Agora explore a documentação da função input().
