# Strings

## Criação

Em Python, strings são demarcadas por aspas, tanto simples (') quanto duplas ("), mas somente uma ou outra dentro de uma string. Preferencialmente usamos aspas simples. Há um caso especial, utilizando aspas triplas (''' ou """), que é utilizado para mútiplas linhas de texto. Na maioria das vezes as aspas triplas são utilizadas para documentação do código.

Exemplos de aspas simples:

```python
# Exemplo de string com aspas simples
string1 = 'Olá, mundo!'

# Uso de aspas simples dentro da string
string2 = 'Ele disse: "Python é incrível!"'

# String vazia com aspas simples
string3 = ''

```

Exemplos de aspas duplas:

```python
# Exemplo de string com aspas duplas
string1 = "Olá, mundo!"

# Uso de aspas duplas dentro da string
string2 = "Ele disse: 'Python é incrível!'"

# String vazia com aspas duplas
string3 = ""

```

Exemplos de aspas triplas

```python
# Exemplo de string multilinhas com aspas triplas
string1 = """Este é um exemplo
de uma string multilinhas."""

# Uso de aspas simples e duplas dentro da string multilinhas
string2 = """Ele disse: "Python é incrível!""""

# String vazia com aspas triplas
string3 = """
"""

# String multilinhas sem conteúdo
string4 = """
Este é um exemplo de uma string multilinhas vazia.
"""

```

## Acesso à posições

Em Python, as strings são imutáveis, o que significa que elas não podem ser modificadas depois de serem criadas. Quando você realiza operações de manipulação de strings, como concatenação, fatiamento ou substituição de caracteres, na verdade está criando uma nova string com as alterações desejadas.

### Operador de Índice

Você pode acessar caracteres individuais em uma string usando a indexação. Em Python, a indexação começa em 0 para o primeiro caractere. O operador de indice é o [ ]

Aqui está um exemplo:

```python
fruta = "banana"

primeira_letra = fruta[0]
print(primeira_letra)  # Saída: b

segunda_letra = fruta[1]
print(segunda_letra)  # Saída: a

```

Caso atribuirmos um novo valor à uma das posições de uma string teremos um erro. Veja o exemplo a seguir:

```python
mensagem = "Olá, mundo!"

mensagem[0] = 'H' # Isso resultará em um erro

```

A imutabilidade de strings tem algumas vantagens, como garantir a integridade dos dados e a segurança em ambientes compartilhados ou concorrentes. Além disso, essa propriedade permite otimizações internas, já que strings imutáveis podem ser armazenadas em cache e compartilhadas por várias partes do programa.

Além dos índices positivos, você também pode usar índices negativos para acessar elementos a partir do final da sequência. O índice -1 refere-se ao último elemento, -2 ao penúltimo e assim por diante. Por exemplo:

```python
mensagem = "Olá"
print(mensagem[-1])  # Saída: 'á'
print(mensagem[-2])  # Saída: 'l'
print(mensagem[-3])  # Saída: 'O'

```

Se você tentar acessar um índice que está fora do intervalo válido, Python lançará um erro chamado IndexError. É importante garantir que os índices estejam dentro dos limites.

### Fatiar uma string (sub-string).

O fatiamento é feito usando a notação [começo:fim]. O caractere no índice "começo" está incluído, mas o caractere no índice "fim" não está incluído. Embora o termo fatiar se pareça com recortar, a string original permanece imutável. Uma nova string é gerada, também chamada de sub-string.

Aqui estão alguns exemplos:

```python
fruta = "banana"

parte = fruta[0:3]
print(parte) # Saída: ban

```

Você também pode usar índices negativos com o operador de fatiamento. Os índices negativos referem-se a elementos contados a partir do final da sequência. Por exemplo

```python
sequencia = "Python"
print(sequencia[-3:-1])  # Saída: "ho"

```

Se você omitir o "começo" no operador de fatiamento, o fatiamento começará do início da sequência. Se você omitir o "fim", o fatiamento irá até o final da sequência. Por exemplo:

```python
sequencia = "Python"
print(sequencia[:3])  # Saída: "Pyt"
print(sequencia[3:])  # Saída: "hon"
```

Você também pode especificar um valor de passo (step) no operador de fatiamento para pular elementos na sequência. O padrão é 1, mas você pode usar outros valores para avançar em diferentes intervalos.

```python
sequencia = "Python"
print(sequencia[::2]) # Saída: "Pto"
```

Uma forma de uso comum do operador de fatiamento é para inverter uma string a partir do último caractere. Veja o exemplo:

```python
sequencia = "Python"
print(sequencia[::-1]) # nohtyP
```

## Formatando Strings

A formatação de strings é uma técnica muito útil no Python para criar strings dinâmicas combinando texto estático com valores de variáveis.

### Concatenar

A concatenação de strings na linguagem Python é a operação de combinar duas ou mais strings em uma única string. Você pode realizar a concatenação de strings usando o operador de adição (+) ou usando o recurso de formatação de strings. Veja um exemplo do uso do operador de adição:

```python
nome = "João"
sobrenome = "Silva"

nome_completo = nome + " " + sobrenome
print(nome_completo) # Saída: João Silva

```

### Caracteres de Escape

Um escape sequence é um conjunto de caracteres, geralmente precedidos por uma barra para a esquerda (\) que possuem um significado especial. É bastante útil que você se familiarize com esses caracteres, pois eles podem ajudá-lo muito na hora de consertar arquivos de texto.

- \n: Cria uma nova linha
- \t: Cria um tab
- \r: Retorna ao início da linha
- \\: Escreve a barra para a esquerda em si.

### Raw Strings

Suponha que você deseja imprimir justamente a string 'Hello\nworld!', sem separação de texto. Isso pode ser feito utilizando uma raw string, que é criada simplesmente colocando um r antes das aspas.

```python
print(r'Hello\nworld!')
print(r'\abc')
```

### f-strings

Também chamadas de f-strings pois são strings com a letra f no início e chaves {} para realizar a interpolação de expressões.

```python
nome = "Alice"
idade = 25
altura = 1.65

mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos. Minha altura é {altura} metros."
print(mensagem)
```

Também é possível realizar formatação mais avançada dentro das chaves das f-strings. Aqui estão alguns exemplos

```python
numero = 42
pi = 3.14159

print(f"O número é {numero:03d}")  # Resultado: O número é 042
print(f"O valor de pi é {pi:.2f}")  # Resultado: O valor de pi é 3.14
```

Com f-strings, você pode alinhar strings para formatar sua saída de maneira mais organizada. É possível especificar o alinhamento à esquerda, à direita ou centralizado dentro de um campo de largura fixa. Isso é feito adicionando um sinal de dois-pontos após a expressão dentro das chaves e, em seguida, especificando o tipo de alinhamento e a largura desejada.

Aqui está um exemplo de como alinhar strings com f-strings:

```python
valor = 42.123456789

print(f"Valor: {valor:<10.2f}")  # Alinhado à esquerda com 2 casas decimais
print(f"Valor: {valor:>10.2f}")  # Alinhado à direita com 2 casas decimais
print(f"Valor: {valor:^10.2f}")  # Centralizado com 2 casas decimais

```

Ainda é possível formatar datas, portentagens, notações numérica e alinhar texto.

### Operador de formatação %

Neste exemplo, %s é usado como marcador de posição para uma string, e %d é usado como marcador de posição para um número inteiro.Esta forma é baseada na formatação da linguagem C.

```python
nome = "Alice"
idade = 25

mensagem = "Olá, meu nome é %s e eu tenho %d anos." % (nome, idade)
print(mensagem)
```

### Método str.format()

O método .format() permite inserir valores em uma string usando marcadores de posição. Foi introduzido no Python 2.6. Aqui está um exemplo básico:

```python
nome = "Alice"
idade = 25
altura = 1.65

mensagem = "Olá, meu nome é {} e eu tenho {} anos. Minha altura é {} metros.".format(nome, idade, altura)
print(mensagem)
```

## Métodos

Python possui várias funções e métodos integrados que facilitam a manipulação de strings. Aqui estão alguns exemplos:

1.  Função len():

    A função len() retorna o comprimento de uma string, ou seja, o número de caracteres presentes nela. Aqui está um exemplo de uso:

    ```python
    mensagem = "Olá, mundo!"
    comprimento = len(mensagem)
    print(comprimento)  # Saída: 13

    ```

2.  Método upper() e lower():

    O método upper() converte uma string para letras maiúsculas, enquanto o método lower() converte uma string para letras minúsculas. Aqui está um exemplo:

    ```python
    mensagem = "Python é incrível!"
    maiusculas = mensagem.upper()
    minusculas = mensagem.lower()
    print(maiusculas)  # Saída: PYTHON É INCRÍVEL!
    print(minusculas)  # Saída: python é incrível!

    ```

3.  Método strip():

    O método strip() remove espaços em branco no início e no final de uma string. É útil para limpar entradas de texto que podem conter espaços extras. Aqui está um exemplo:

    ```python
    texto = "    Olá, mundo!    "
    texto_limpo = texto.strip()
    print(texto_limpo) # Saída: "Olá, mundo!"
    ```

4.  Método split():

    O método split() divide uma string em substrings com base em um separador especificado. O resultado é uma lista de substrings. Aqui está um exemplo:

    ```python
    frase = "Python é uma linguagem poderosa"
    palavras = frase.split()
    print(palavras)  # Saída: ['Python', 'é', 'uma', 'linguagem', 'poderosa']
    ```

    Você também pode especificar um separador personalizado usando o método split(). Por exemplo:

    ```python
    data = "2023-07-14"

    partes = data.split("-")
    print(partes) # Saída: ['2023', '07', '14']
    ```

5.  Método replace()

    O método replace() substitui todas as ocorrências de uma substring por outra substring em uma string. Aqui está um exemplo:

    ```python
    mensagem = "Python é incrível!"
    nova_mensagem = mensagem.replace("incrível", "fantástico")
    print(nova_mensagem)  # Saída: "Python é fantástico!"
    ```

Esses são apenas alguns exemplos de funções e métodos para a manipulação de strings em Python. Existem muitos outros disponíveis, como find(), count(), startswith(), endswith(), join(), entre outros.
