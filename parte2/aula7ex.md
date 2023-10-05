1. Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, \[nome\]!".
2. Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.
3. Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. O idioma é opcional e padrão para "inglês". A função deve retornar uma saudação no idioma especificado.
4. Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente
5. Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. Forneça uma documentação que explique como usar a função e inclua exemplos de uso.
6. Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.
7. Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. Forneça uma documentação estendida que explique como usar a função e inclua exemplos de uso.
8. Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido. Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com
9. Escreva uma função calcular_pagamento que aceita os parâmetros nomeados horas_trabalhadas e taxa_hora e retorna o pagamento total.
10. Crie uma função que retorne o maior número dentre 3 elementos.
11. Escreva uma função em Python function que aceita uma string e retorna a quantidade de letras maiúsculas e minúsculas.
12. Crie uma função chamada len_custom que aceita um iterável (por exemplo, uma lista ou uma string) como argumento e retorna o número de elementos no iterável. Ela deve ter o mesmo comportamento que a função embutida len().
13. Crie uma função chamada sum_custom que aceita uma lista de números como argumento e retorna a soma de todos os números na lista. Ela deve ter o mesmo comportamento que a função embutida sum().
14. Crie uma função chamada max_custom que aceita uma lista de números como argumento e retorna o maior número na lista. Ela deve ter o mesmo comportamento que a função embutida max().
15. Crie uma função chamada min_custom que aceita uma lista de números como argumento e retorna o menor número na lista. Ela deve ter o mesmo comportamento que a função embutida min().
16. Crie uma função chamada startswith_custom que aceita uma string e um prefixo como argumentos e retorna True se a string começar com o prefixo, caso contrário, retorna False. Ela deve ter o mesmo comportamento que o método str.startswith().
17. Crie uma função chamada endswith_custom que aceita uma string e um sufixo como argumentos e retorna True se a string terminar com o sufixo, caso contrário, retorna False. Ela deve ter o mesmo comportamento que o método str.endswith().
18. Crie uma função chamada split_custom que aceita uma string e um caractere de separação como argumentos e retorna uma lista de substrings separadas pelo caractere de separação. Ela deve ter o mesmo comportamento que o método str.split().
19. Crie uma função chamada strip_custom que aceita uma string e caracteres de remoção como argumentos e retorna uma nova string com os caracteres de remoção removidos dos extremos da string. Ela deve ter o mesmo comportamento que o método str.strip().
20. Crie uma função chamada replace_custom que aceita uma string, uma substring antiga e uma substring nova como argumentos e retorna uma nova string com todas as ocorrências da substring antiga substituídas pela substring nova. Ela deve ter o mesmo comportamento que o método str.replace().

Utilize os casos de teste a seguir para validar seu código:

```

# Teste para a função saudacao
@pytest.mark.parametrize("nome, saudacao_esperada", [("Alice", "Olá, Alice!"), ("Bob", "Olá, Bob!")])
def test_saudacao(nome, saudacao_esperada):
    assert saudacao(nome) == saudacao_esperada

# Teste para a função dobro
@pytest.mark.parametrize("numero, resultado_esperado", [(2, 4), (0, 0), (-2, -4)])
def test_dobro(numero, resultado_esperado):
    assert dobro(numero) == resultado_esperado

# Teste para a função saudacao_personalizada
@pytest.mark.parametrize("nome, idioma, saudacao_esperada", [("Alice", "inglês", "Hello, Alice!"), ("Bob", "espanhol", "Hola, Bob!"), ("Charlie", "francês", "Bonjour, Charlie!")])
def test_saudacao_personalizada(nome, idioma, saudacao_esperada):
    assert saudacao_personalizada(nome, idioma) == saudacao_esperada

# Teste para a função potencia
@pytest.mark.parametrize("base, expoente, resultado_esperado", [(2, 3, 8), (5, 2, 25), (3, 0, 1)])
def test_potencia(base, expoente, resultado_esperado):
    assert potencia(base, expoente) == resultado_esperado

# Teste para a função idade_valida
@pytest.mark.parametrize("idade, resultado_esperado", [(25, True), (0, True), (200, False)])
def test_idade_valida(idade, resultado_esperado):
    assert idade_valida(idade) == resultado_esperado

# Teste para a função validar_email
@pytest.mark.parametrize("email, resultado_esperado", [("exemplo@email.com", True), ("invalido@.com", False), ("sem_arroba.com", False)])
def test_validar_email(email, resultado_esperado):
    assert validar_email(email) == resultado_esperado

# Teste para a função calcular_pagamento
@pytest.mark.parametrize("horas_trabalhadas, taxa_hora, resultado_esperado", [(40, 10, 400), (0, 15, 0), (45, 12.5, 562.5)])
def test_calcular_pagamento(horas_trabalhadas, taxa_hora, resultado_esperado):
    assert calcular_pagamento(horas_trabalhadas=horas_trabalhadas, taxa_hora=taxa_hora) == resultado_esperado

# Teste para a função que retorna o maior número dentre 3 elementos
@pytest.mark.parametrize("a, b, c, resultado_esperado", [(5, 2, 8, 8), (-10, -20, -5, -5), (3, 3, 3, 3)])
def test_maior_numero(a, b, c, resultado_esperado):
    assert maior_numero(a, b, c) == resultado_esperado

# Teste para a função que retorna a quantidade de letras maiúsculas e minúsculas
@pytest.mark.parametrize("entrada, resultado_esperado", [("Hello World", (2, 8)), ("AbCDeF", (3, 3)), ("12345", (0, 0))])
def test_contagem_letras(entrada, resultado_esperado):
    assert contagem_letras(entrada) == resultado_esperado

# Teste para a função len_custom
@pytest.mark.parametrize("iteravel, resultado_esperado", [([1, 2, 3], 3), ("Python", 6), ("", 0)])
def test_len_custom(iteravel, resultado_esperado):
    assert len_custom(iteravel) == resultado_esperado

# Teste para a função sum_custom
@pytest.mark.parametrize("lista_numeros, resultado_esperado", [([1, 2, 3], 6), ([], 0), ([-1, -2, -3], -6)])
def test_sum_custom(lista_numeros, resultado_esperado):
    assert sum_custom(lista_numeros) == resultado_esperado

# Teste para a função max_custom
@pytest.mark.parametrize("lista_numeros, resultado_esperado", [([1, 2, 3], 3), ([], None), ([-1, -2, -3], -1)])
def test_max_custom(lista_numeros, resultado_esperado):
    assert max_custom(lista_numeros) == resultado_esperado

# Teste para a função min_custom
@pytest.mark.parametrize("lista_numeros, resultado_esperado", [([1, 2, 3], 1), ([], None), ([-1, -2, -3], -3)])
def test_min_custom(lista_numeros, resultado_esperado):
    assert min_custom(lista_numeros) == resultado_esperado

# Teste para a função startswith_custom
@pytest.mark.parametrize("string, prefixo, resultado_esperado", [("Python is fun", "Python", True), ("Hello, world!", "world", False), ("12345", "12", True)])
def test_startswith_custom(string, prefixo, resultado_esperado):
    assert startswith_custom(string, prefixo) == resultado_esperado

# Teste para a função endswith_custom
@pytest.mark.parametrize("string, sufixo, resultado_esperado", [("Python is fun", "fun", True), ("Hello, world!", "Hello", False), ("12345", "45", True)])
def test_endswith_custom(string, sufixo, resultado_esperado):
    assert endswith_custom(string, sufixo) == resultado_esperado

# Teste para a função split_custom
@pytest.mark.parametrize("string, caractere, resultado_esperado", [("Python is fun", " ", ["Python", "is", "fun"]), ("Hello,world!", ",", ["Hello", "world!"]), ("12345", "3", ["12", "45"])])
def test_split_custom(string, caractere, resultado_esperado):
    assert split_custom(string, caractere) == resultado_esperado

# Teste para a função strip_custom
@pytest.mark.parametrize("string, caracteres_remover, resultado_esperado", [("   Python   ", " ", "Python"), ("***Hello,world!***", "*", "Hello,world!"), ("###12345###", "#", "12345")])
def test_strip_custom(string, caracteres_remover, resultado_esperado):
    assert strip_custom(string, caracteres_remover) == resultado_esperado

# Teste para a função replace_custom
@pytest.mark.parametrize("string, substring_antiga, substring_nova, resultado_esperado", [("Python is fun", "fun", "awesome", "Python is awesome"), ("Hello, world!", "world", "universe", "Hello, universe!"), ("12345", "3", "7", "12745")])
def test_replace_custom(string, substring_antiga, substring_nova, resultado_esperado):
    assert replace_custom(string, substring_antiga, substring_nova) == resultado_esperado


```
