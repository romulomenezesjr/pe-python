# Módulos Python


## Definição

Um módulo é um arquivo que contém definições e instruções de Python. Um módulo pode conter funções, classes e variáveis que você pode reutilizar em diferentes programas. Ele ajuda a organizar o código, tornando-o mais legível e modular.

Os módulos podem ser criados por você ou podem ser módulos internos da biblioteca padrão de Python, ou até mesmo pacotes de terceiros que você instala.

## Exemplos

Para usar as funcionalidades de um módulo, você precisa importá-lo no seu código. A forma básica de fazer isso é usando a palavra-chave import.

Exemplo 1: Importando um módulo da biblioteca padrão
Vamos importar o módulo math, que contém funções matemáticas como sqrt (para raiz quadrada) e pi (constante matemática).

```py
import math

# Usando uma função do módulo math
resultado = math.sqrt(16)
print(resultado)  # Saída: 4.0

```


Exemplo 2: Importando uma função específica de um módulo
Você também pode importar apenas uma função específica de um módulo, assim:

```py
from math import sqrt

# Usando diretamente a função sqrt
resultado = sqrt(25)
print(resultado)  # Saída: 5.0

```

## Criando o seu próprio módulo
Você pode criar seus próprios módulos escrevendo funções ou classes em um arquivo Python (.py). Depois, pode importar esse módulo em outros arquivos Python.

Exemplo 1: Criando um módulo
Crie um arquivo chamado meu_modulo.py com o seguinte conteúdo
```py
# meu_modulo.py

def saudacao(nome):
    return f"Olá, {nome}!"

def soma(a, b):
    return a + b

```


Agora, em outro arquivo Python, você pode importar e usar as funções do seu módulo:
```py
# outro_arquivo.py

import meu_modulo

print(meu_modulo.saudacao("Maria"))
print(meu_modulo.soma(5, 3))
```

## Módulos da Biblioteca Padrão

Python vem com uma série de módulos que você pode usar sem precisar instalar nada adicionalmente. Alguns exemplos de módulos úteis da biblioteca padrão:

- os: para interagir com o sistema operacional (ex: manipulação de arquivos e diretórios)
- datetime: para trabalhar com datas e horas
- random: para gerar números aleatórios
- sys: para manipulação de parâmetros de execução do script
- json: para trabalhar com dados no formato JSON



## PIP

A instalação de módulos externos aos da biblioteca padrão do python é feita utilizando a ferramenta pip  (Python Package Installer). Ele é o gerenciador de pacotes do Python e permite instalar, atualizar e remover bibliotecas e dependências de projetos Python diretamente do PyPI (Python Package Index).

### Verificar se o pip está instalado
```sh
pip --version

```

Se não estiver instalado, você pode instalá-lo com:
```sh
python -m ensurepip --default-pip
```

Os módulos instalados pelo pip são armazenados dentro do diretório site-packages do ambiente Python que está sendo usado.

### Instalar um pacote

```sh
pip install nome-do-pacote

```

### Atualizar um pacote
```sh
pip install --upgrade pandas
```

### Verificar onde um pacote foi instalado
```sh
pip show numpy
```
A saída será: 

        Name: numpy
        Version: 1.21.0
        Location: /usr/local/lib/python3.10/site-packages

Em sistemas Linux/macOS (fora de ambientes virtuais) os módulos geralmente ficam em:
```sh
/usr/local/lib/pythonX.Y/site-packages/

~/.local/lib/pythonX.Y/site-packages/
```

Em Windows (fora de ambientes virtuais) os pacotes ficam dentro da pasta do Python instalado, geralmente em:

```sh
C:\Users\SeuUsuário\AppData\Local\Programs\Python\PythonX.Y\Lib\site-packages\
```
## Ambientes Virtuais

Ambientes virtuais permitem que você isole as dependências de cada projeto, evitando conflitos entre versões de pacotes. Assim, diferentes projetos podem usar versões distintas de bibliotecas sem interferir entre si.

Para criar um ambiente virtual, navegue até o diretório onde deseja criar o ambiente e execute o seguinte comando no terminal:

```sh
python -m venv nome_do_ambiente
```

Isso cria uma pasta chamada nome_do_ambiente com a estrutura do ambiente virtual dentro dela.

Depois de criar o ambiente virtual, você precisa ativá-lo para começar a usá-lo. A ativação depende do sistema operacional.

- Windows:
```sh
meu_ambiente\Scripts\activate
```
- macOS/Linux:
```sh
source meu_ambiente/bin/activate
```

Quando o ambiente virtual estiver ativado, você verá o nome do ambiente na linha de comando, indicando que o Python está isolado nesse ambiente. Algo como:

 ```sh
(meu_ambiente) $
```

Agora, qualquer pacote que você instalar será instalado somente dentro do ambiente virtual, sem afetar o Python global do sistema.

### Instalação de Pacotes em Ambientes Virtuais

Com o ambiente virtual ativado, você pode instalar pacotes usando o pip (o gerenciador de pacotes do Python).

Por exemplo, para instalar o pacote requests, use

```sh
pip install requests
```



Quando você tiver instalado todos os pacotes necessários no seu ambiente virtual, pode gerar um arquivo requirements.txt para documentar as dependências do projeto. Esse arquivo lista todos os pacotes e suas versões.

Para criar o requirements.txt, execute:
```sh
pip freeze > requirements.txt
```


Isso gera um arquivo requirements.txt com todas as dependências do seu ambiente virtual. Esse arquivo pode ser compartilhado com outras pessoas ou usado em outro ambiente para instalar as mesmas dependências

### Instalar dependências a partir do requirements.txt

Se você ou alguém precisar recriar o ambiente virtual em outra máquina, basta usar o requirements.txt para instalar todas as dependências de uma vez.

Para instalar as dependências de um projeto, basta executar
```sh
pip install -r requirements.txt
```

### Desativar o ambiente virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o comando:

```sh
deactivate
```
## Principais Módulos

Aqui está uma lista de diversos módulos Python, com uma breve descrição e o link para a documentação oficial:  

---

### 1. **requests**  
O `requests` é um módulo popular para fazer requisições HTTP de forma simples e intuitiva. Ele permite enviar e receber dados da web, tornando-o ideal para consumir APIs e automatizar interações com sites.  
📌 [Documentação Oficial](https://docs.python-requests.org/en/latest/)  

### 2. **pandas**  
O `pandas` é uma biblioteca essencial para manipulação e análise de dados. Ele fornece estruturas como `DataFrame` e `Series`, facilitando a organização, limpeza e transformação de conjuntos de dados grandes.  
📌 [Documentação Oficial](https://pandas.pydata.org/docs/)  

### 3. **numpy**  
O `numpy` é uma biblioteca fundamental para computação numérica em Python. Ele fornece suporte para arrays multidimensionais, funções matemáticas avançadas e operações vetorizadas de alta performance.  
📌 [Documentação Oficial](https://numpy.org/doc/)  

### 4. **matplotlib**  
O `matplotlib` é uma biblioteca para criação de gráficos e visualizações de dados. Ele permite gerar gráficos de linha, dispersão, histogramas e muito mais, sendo amplamente usado em ciência de dados.  
📌 [Documentação Oficial](https://matplotlib.org/stable/contents.html)  

### 5. **seaborn**  
O `seaborn` é uma biblioteca baseada no `matplotlib`, focada na criação de visualizações estatísticas atraentes e informativas. Ele simplifica a geração de gráficos complexos e melhora a estética padrão.  
📌 [Documentação Oficial](https://seaborn.pydata.org/)  

### 6. **flask**  
O `flask` é um microframework para desenvolvimento de aplicações web em Python. Ele é leve, flexível e fácil de aprender, ideal para criar APIs e aplicações web simples.  
📌 [Documentação Oficial](https://flask.palletsprojects.com/en/latest/)  

### 7. **django**  
O `django` é um framework robusto para desenvolvimento web, seguindo o padrão MVC. Ele inclui recursos como autenticação, ORM e administração integrada, facilitando o desenvolvimento de aplicações escaláveis.  
📌 [Documentação Oficial](https://docs.djangoproject.com/en/stable/)  

### 8. **tkinter**  
O `tkinter` é a biblioteca padrão do Python para criação de interfaces gráficas (GUI). Ele permite desenvolver aplicativos de desktop com botões, caixas de entrada, menus e muito mais.  
📌 [Documentação Oficial](https://docs.python.org/3/library/tkinter.html)  

### 9. **scikit-learn**  
O `scikit-learn` é uma biblioteca poderosa para aprendizado de máquina. Ele oferece algoritmos de classificação, regressão, agrupamento e outras técnicas de inteligência artificial.  
📌 [Documentação Oficial](https://scikit-learn.org/stable/documentation.html)  

### 10. **opencv (cv2)**  
O `opencv` é uma biblioteca de visão computacional e processamento de imagens. Ele é utilizado para reconhecimento facial, detecção de objetos, filtragem de imagens e outras aplicações.  
📌 [Documentação Oficial](https://docs.opencv.org/master/)  

### 11. **pillow**  
O `pillow` é uma biblioteca para manipulação de imagens em Python. Ele permite abrir, editar, redimensionar e aplicar filtros em arquivos de imagem de diversos formatos.  
📌 [Documentação Oficial](https://pillow.readthedocs.io/en/stable/)  

### 12. **beautifulsoup4**  
O `beautifulsoup4` é uma biblioteca para web scraping, permitindo extrair e manipular dados de páginas HTML e XML de forma simples.  
📌 [Documentação Oficial](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  

### 13. **sqlite3**  
O `sqlite3` é um módulo embutido no Python que permite interagir com bancos de dados SQLite. Ele é útil para armazenar e manipular dados estruturados sem necessidade de um servidor de banco de dados.  
📌 [Documentação Oficial](https://docs.python.org/3/library/sqlite3.html)  

### 14. **pyttsx3**  
O `pyttsx3` é uma biblioteca de conversão de texto para fala (TTS), permitindo que programas Python gerem áudio falado a partir de strings de texto.  
📌 [Documentação Oficial](https://pyttsx3.readthedocs.io/en/latest/)  

### 15. **pygame**  
O `pygame` é uma biblioteca para desenvolvimento de jogos em Python. Ele fornece suporte para gráficos, sons e interação com teclado e mouse, facilitando a criação de jogos 2D.  
📌 [Documentação Oficial](https://www.pygame.org/docs/)  

### 16. **asyncio**  
O `asyncio` é um módulo da biblioteca padrão do Python para programação assíncrona. Ele permite a execução de múltiplas tarefas simultaneamente, sendo útil para servidores, bots e aplicações de rede.  
📌 [Documentação Oficial](https://docs.python.org/3/library/asyncio.html)  

### 17. **pyautogui**  
O `pyautogui` é uma biblioteca para automação de interface gráfica, permitindo controlar o mouse e o teclado para interagir com aplicativos automaticamente.  
📌 [Documentação Oficial](https://pyautogui.readthedocs.io/en/latest/)  

### 18. **cryptography**  
O `cryptography` fornece ferramentas para implementar técnicas de segurança, como criptografia simétrica e assimétrica, assinaturas digitais e hashing.  
📌 [Documentação Oficial](https://cryptography.io/en/latest/)  

### 19. **pytest**  
O `pytest` é uma biblioteca para criação de testes automatizados em Python, facilitando a verificação de código e garantindo a qualidade dos programas.  
📌 [Documentação Oficial](https://docs.pytest.org/en/latest/)  

### 20. **logging**  
O `logging` é um módulo da biblioteca padrão do Python para geração e gerenciamento de logs. Ele é essencial para depuração e monitoramento de aplicações.  
📌 [Documentação Oficial](https://docs.python.org/3/library/logging.html)  

---

Se precisar de mais sugestões ou quiser um aprofundamento sobre algum desses módulos, é só me avisar! 🚀

## Referências

- https://docs.python.org/pt-br/3.13/tutorial/modules.html