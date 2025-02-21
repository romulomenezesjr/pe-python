# Persistência de Dados em Arquivos em Python

Em Python, a persistência de dados em arquivos é uma técnica comum e eficaz para armazenar informações de forma permanente. Isso permite que os dados sejam recuperados e reutilizados mesmo após o encerramento do programa. Existem várias formas de trabalhar com arquivos em Python, permitindo que você leia e escreva dados em diferentes formatos e estruturas.

## Leitura de Dados de Arquivos

Para ler dados de um arquivo em Python, você pode seguir os seguintes passos:

1. Abrir o arquivo usando a função `open()`, que retorna um objeto de arquivo.
2. Ler o conteúdo do arquivo usando os métodos `read()`, `readline()`, ou `readlines()`, dependendo da forma como os dados estão organizados.

Aqui está um exemplo de como ler o conteúdo de um arquivo de texto:

```python
# Abrir o arquivo para leitura
with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

## Escrita de Dados em Arquivos

Para escrever dados em um arquivo em Python, siga estes passos:

1. Abrir o arquivo usando a função `open()` com o modo de escrita (`'w'`).
2. Escrever os dados no arquivo usando o método `write()`.

Aqui está um exemplo de como escrever dados em um arquivo de texto:

```python
# Dados a serem escritos no arquivo
dados = "Esses são os dados que serão escritos no arquivo."

# Abrir o arquivo para escrita
with open('dados.txt', 'w') as arquivo:
    arquivo.write(dados)
```

### Navegação e Manipulação do Sistema de Arquivos em Python

Python oferece uma variedade de bibliotecas que permitem a navegação e manipulação do sistema de arquivos, tornando a tarefa de lidar com diretórios e arquivos uma tarefa fácil e poderosa. Algumas das bibliotecas mais comuns são `os`, `shutil` e `glob`. Vamos explorar cada uma delas:

# O Módulo "os" em Python

O módulo "os" é uma das bibliotecas mais poderosas em Python para interagir com o sistema operacional. Ele fornece várias funções que permitem navegar e manipular o sistema de arquivos, executar comandos do sistema operacional, obter informações sobre o ambiente de execução, entre outras tarefas relacionadas ao sistema. Aqui estão alguns dos principais recursos do módulo "os":

## Obter Informações do Sistema Operacional

- `os.name`: Retorna o nome do sistema operacional (exemplo: 'posix' para sistemas UNIX e 'nt' para Windows).
- `os.uname()`: Retorna informações detalhadas do sistema em sistemas UNIX (Linux, macOS, etc.).

## Navegação e Manipulação de Diretórios

- `os.getcwd()`: Retorna o diretório de trabalho atual.

  ```python
  import os

  diretorio_atual = os.getcwd()
  print(diretorio_atual)
  ```

- `os.chdir(caminho)`: Muda o diretório de trabalho atual para o caminho especificado.

  ```python
  import os

  novo_diretorio = '/caminho/para/o/diretorio'
  os.chdir(novo_diretorio)
  ```

- `os.listdir(caminho)`: Lista os arquivos e diretórios no caminho especificado.

  ```python
  import os

  diretorio = '/caminho/para/o/diretorio'
  conteudo = os.listdir(diretorio)
  print(conteudo)
  ```

- `os.mkdir(nome_diretorio)`: Cria um novo diretório com o nome especificado.
- `os.makedirs(caminho)`: Cria diretórios recursivamente com base no caminho especificado.
- `os.rmdir(nome_diretorio)`: Remove um diretório vazio com o nome especificado.
- `os.removedirs(caminho)`: Remove diretórios vazios recursivamente com base no caminho especificado.
- `os.rename(antigo_nome, novo_nome)`: Renomeia um arquivo ou diretório.
- `os.remove(nome_arquivo)`: Remove um arquivo.

## Execução de Comandos do Sistema Operacional

- `os.system(comando)`: Executa um comando do sistema operacional (pode ser inseguro devido a vulnerabilidades de segurança).
- `os.popen(comando)`: Executa um comando do sistema operacional e retorna um objeto que permite ler a saída do comando.

## Verificação de Existência de Arquivos e Diretórios

- `os.path.exists(caminho)`: Verifica se um caminho (arquivo ou diretório) existe.
- `os.path.isfile(caminho)`: Verifica se o caminho é um arquivo.
- `os.path.isdir(caminho)`: Verifica se o caminho é um diretório.
- `os.path.abspath(caminho)`: Retorna o caminho absoluto do caminho fornecido.

## Manipulação de Caminhos

- `os.path.join(caminho1, caminho2, ...)`: Une caminhos para formar um caminho completo de acordo com o sistema operacional.
- `os.path.split(caminho)`: Separa o caminho em uma tupla (diretório, arquivo).

Essas são apenas algumas das funções disponíveis no módulo "os". É importante lembrar que algumas funções do "os" podem ser específicas do sistema operacional, portanto, é recomendável verificar a documentação oficial do Python para obter informações detalhadas e garantir a portabilidade do código.

# Biblioteca `shutil`

A biblioteca `shutil` fornece funções para trabalhar com arquivos e diretórios de uma forma mais eficiente e segura. Em particular as funções de cópia, movimentação e remoção. Aqui estão algumas funções úteis:

1. Copiar um arquivo:

```python
import shutil

origem = 'arquivo_origem.txt'
destino = 'caminho/para/destino/arquivo_destino.txt'
shutil.copy(origem, destino)
```

2. Copiar um diretório e todo o seu conteúdo:

```python
import shutil

origem = 'diretorio_origem'
destino = 'caminho/para/destino/diretorio_destino'
shutil.copytree(origem, destino)
```

3. Mover um arquivo ou diretório:

```python
import shutil

origem = 'arquivo_ou_diretorio'
destino = 'caminho/para/destino/'
shutil.move(origem, destino)
```

# Biblioteca `glob`

A biblioteca `glob` é útil para buscar arquivos e diretórios com base em padrões de nome. Ela usa caracteres especiais como '\*' e '?' para representar curingas. Aqui está um exemplo:

```python
import glob

arquivos_txt = glob.glob('diretorio/*.txt')
print(arquivos_txt)
```

Esta é apenas uma introdução à navegação e manipulação do sistema de arquivos em Python. Com essas bibliotecas, você pode criar scripts para automatizar tarefas relacionadas a arquivos e diretórios, como criar pastas, renomear arquivos, excluir arquivos e muito mais. Lembre-se de usar essas funções com cuidado, pois as ações de manipulação do sistema de arquivos podem ser irreversíveis e afetar outros processos do sistema.

# Manipulação de Arquivos JSON e CSV em Python

Python oferece suporte nativo para a manipulação de arquivos JSON (JavaScript Object Notation) e CSV (Comma-Separated Values), que são formatos amplamente usados para armazenar e trocar dados estruturados. Vamos explorar como ler e escrever arquivos JSON e CSV em Python:

## Manipulação de Arquivos JSON

### Leitura de Arquivos JSON:

Para ler dados de um arquivo JSON, podemos utilizar a biblioteca padrão `json`. Ela nos permite carregar os dados do arquivo em uma estrutura de dados Python, geralmente listas e dicionários.

```python
import json

# Leitura de dados do arquivo JSON
with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

print(dados)
```

### Escrita de Arquivos JSON:

Para escrever dados em um arquivo JSON, também utilizamos a biblioteca `json`. Precisamos garantir que os dados que queremos escrever sejam estruturas compatíveis com JSON, como listas e dicionários.

```python
import json

# Dados a serem escritos em um arquivo JSON
dados = {
    'nome': 'Alice',
    'idade': 30,
    'profissao': 'Engenheira'
}

# Escrita de dados no arquivo JSON
with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)
```

## Manipulação de Arquivos CSV

### Leitura de Arquivos CSV:

Para ler dados de um arquivo CSV, podemos utilizar a biblioteca padrão `csv`. Ela nos permite ler os dados do arquivo e transformá-los em listas ou dicionários, dependendo da estrutura do arquivo.

```python
import csv

# Leitura de dados do arquivo CSV em formato de lista
with open('dados.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)
```

Para ler os dados em formato de dicionário, podemos usar o `DictReader`:

```python
import csv

# Leitura de dados do arquivo CSV em formato de dicionário
with open('dados.csv', 'r') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)
```

### Escrita de Arquivos CSV:

Para escrever dados em um arquivo CSV, também utilizamos a biblioteca `csv`. Podemos usar o `writer` para escrever listas ou o `DictWriter` para escrever dicionários.

```python
import csv

# Dados a serem escritos em um arquivo CSV
dados = [
    ['Nome', 'Idade', 'Profissão'],
    ['Alice', 30, 'Engenheira'],
    ['Bob', 25, 'Desenvolvedor']
]

# Escrita de dados no arquivo CSV usando o writer
with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)
```

Para escrever os dados em formato de dicionário, podemos usar o `DictWriter`:

```python
import csv

# Dados a serem escritos em um arquivo CSV
dados = [
    {'Nome': 'Alice', 'Idade': 30, 'Profissão': 'Engenheira'},
    {'Nome': 'Bob', 'Idade': 25, 'Profissão': 'Desenvolvedor'}
]

# Escrita de dados no arquivo CSV usando o DictWriter
campos = ['Nome', 'Idade', 'Profissão']
with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor_csv.writeheader()
    escritor_csv.writerows(dados)
```

Essas são as principais técnicas para manipulação de arquivos JSON e CSV em Python. Esses formatos são amplamente usados para armazenar e compartilhar dados, e o Python oferece uma ótima biblioteca padrão para facilitar seu uso e manipulação. Lembre-se de sempre verificar a documentação oficial para obter mais detalhes sobre as funções e opções disponíveis em `json` e `csv`.

# Pickle e Marshal em Python

Tanto o módulo `pickle` quanto o módulo `marshal` em Python são usados para a serialização e desserialização de objetos, mas eles têm algumas diferenças importantes em suas funcionalidades e usos. Vamos explorar cada um deles:

## Pickle

O módulo `pickle` em Python é uma ferramenta poderosa para serializar e desserializar objetos Python em um formato binário. Ele permite que você salve objetos complexos, como listas, dicionários, classes personalizadas, entre outros, em arquivos ou mesmo em uma transmissão de rede.

### Serialização com Pickle:

```python
import pickle

# Dados a serem serializados em um arquivo
dados = [1, 2, 3, 4]

# Serialização com pickle
with open('dados.pkl', 'wb') as arquivo:
    pickle.dump(dados, arquivo)
```

### Desserialização com Pickle:

```python
import pickle

# Desserialização com pickle
with open('dados.pkl', 'rb') as arquivo:
    dados_carregados = pickle.load(arquivo)

print(dados_carregados)  # Output: [1, 2, 3, 4]
```

## Marshal

O módulo `marshal` também é usado para serialização e desserialização de objetos em Python, mas com algumas diferenças significativas em relação ao `pickle`. Ao contrário do `pickle`, o `marshal` não é recomendado para serializar objetos complexos e personalizados. Ele é mais adequado para estruturas de dados simples, como strings, tuplas e listas.

### Serialização com Marshal:

```python
import marshal

# Dados a serem serializados em um arquivo
dados = [1, 2, 3, 4]

# Serialização com marshal
with open('dados.marshal', 'wb') as arquivo:
    marshal.dump(dados, arquivo)
```

### Desserialização com Marshal:

```python
import marshal

# Desserialização com marshal
with open('dados.marshal', 'rb') as arquivo:
    dados_carregados = marshal.load(arquivo)

print(dados_carregados)  # Output: [1, 2, 3, 4]
```

## Diferenças entre Pickle e Marshal

- Pickle é mais versátil e pode serializar objetos complexos, como listas, dicionários e classes personalizadas, enquanto o Marshal é mais adequado para estruturas de dados simples, como strings e listas.

- Pickle produz um formato binário mais legível e geralmente maior, enquanto o formato binário gerado pelo Marshal é mais compacto e menos legível.

- Pickle é compatível entre diferentes versões do Python, permitindo a desserialização de objetos em versões mais recentes e mais antigas. O Marshal, por outro lado, não é garantido ser compatível entre versões diferentes do Python.

## Escolhendo entre Pickle e Marshal

A escolha entre Pickle e Marshal depende das necessidades do seu projeto. Se você precisa serializar objetos complexos e personalizados, o Pickle é a melhor escolha. Por outro lado, se você está trabalhando com estruturas de dados simples e deseja uma serialização mais compacta, o Marshal pode ser uma opção mais adequada.
