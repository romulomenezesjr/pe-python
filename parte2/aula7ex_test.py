import pytest
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

