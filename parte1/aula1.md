# Introdução à Linguagem de Programação Python

## Primeiro Programa

É praticamente uma regra que qualquer curso introdutório de programação mostre o mesmo exemplo: Como mostrar os caracteres "Hello world!" na tela.

```python
print('Hello world!')

```

Para gerar este primeiro programa em Python basta criar um arquivo de texto no Windows, salvar o arquivo com o nome helloworld.py e executar o comando

```sh
python helloworld.py
```

## Linguagens de Programação

**Linguagens de programação são linguagens formais que foram projetadas para execução de instruções lógicas.** Linguagens formais são linguagens diferentes da normal e são usadas para aplicações específicas. Por exemplo, a notação que os matemáticos usam é uma linguagem formal que é particularmente boa para denotar relações entre números e símbolos. Os químicos usam uma linguagem formal para representar a estrutura química das moléculas.

Linguagens formais possuem regras sintáticas e semânticas para descrever o funcionamento e estrutura sem duplo sentido.Também são mais concisas e literais do que a linguagem normal, por isso constuma-se levar um tempo para se acostumar ao seu uso, principalmente se a diferença para a linguagem normal for muito grande.

Ao trabalhar com linguagens de programação você deve compreender quais instruções e qual a lógica para interpretação da máquina. Como são utilizadas para passar instruções que devem ser executadas por máquinas, não consideram contextos ou abstrações, são meros executores. Quem as escreve deve prezar pela objetividade e pelo princípio de funcionamento dos computadores: a eletrônica. Esta trabalha com informações elétricas que são mapeadas para bits (0's e 1's) e operam suas respectivas operações lógicas.

Veja a anedota a seguir e tente imaginar o motivo pelo qual o marido trouxe seis litros de leite.

> A esposa do programador disse:
>
> -Vá ao mercado e traga um litro de leite. Se tiver ovos, traga seis.
>
> O programador voltou com seis litros de leite, então sua esposa disse:
>
> -Programador! Porquê você trouxe seis litros de leite?
>
> E o Programador respondeu:
>
> -Eles tinham ovos...

É fácil compreender que o marido vai ter problemas pois tratou a esposa como máquina.

## Característicass da Linguagem Python

A linguagem Python tem por característica ser muito próxima à linguagem natural. É considerada como uma linguagem de altíssimo nível pois sua estrutura e instruções são de fácil entendimento, considerando o idioma inglês. Toda o conjunto de instruções, forma simplificada de uso e legibilidade a distinguem de outras linguagens de alto nível.

### Alto Níve x Baixo Nível

Também existem as linguagens de baixo nível, às vezes chamadas de "linguagens de máquina" ou "linguagens assembly" (linguagens de montagem). Com muita simplificação podemos dizer que o computador só consegue executar programas escritos em linguagens de baixo nível.

Programas escritos em linguagens de alto nível precisam ser processados antes que possam executar. Esse pré-processamento extra demanda mais tempo, o que é uma pequena desvantagem das linguagens de alto nível. Mas as vantagens são enormes:

- É muito mais fácil programar em uma linguagem de alto nível.
- É mais rápido escrever programas em uma linguagem de alto nível;
- Os programas ficam mais curtos, mais fáceis de ler, mais simples de alterar, e é mais provável que estejam corretos.
- Linguagens de alto nível são portáveis, o que significa que podem rodar em diferentes tipos de computador, com pouca ou nenhuma modificação e programas em baixo nível só podem rodar em um único tipo de computador e precisam ser re-escritos para rodar em outro tipo.

Devido a essas vantagens, quase todos os programas são escritos em linguagens de alto nível. As de baixo nível são utilizadas somente para umas poucas aplicações especializadas.

### Interpretada

Para executar um programa escrito na linguagem Python é necessário ter um programa, também chamado python. Ele é um **interpretador**. Irá verificar e executar cada instrução escrita no seu programa.

Você pode utilizar o interpretador executando instrução por instrução, verificando o resultado individualmente, ou executando um script (python arquivo.py).

No modo interativo cada instrução será executada e gera um retorno, se houver, imediato. Este modo é ótimo para conhecer a linguagem ou explorar recursos de módulos.

```sh
# Interpretador Python
> C:\Users\romulomenezesjr> python3
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> nums = range(1,10)
>>> list(nums)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Ao executar um script com o interpretador Python você deve passar o nome do arquivo à ele. Cada instrução escrita no arquivo deverá ser interpretada uma-a-uma. Veja no exemplo a seguir que existe um erro de tipo, mas como o interpretador não consegue chegar nesta instrução, o erro não é gerado.

```python {.line-numbers .highlight=3}
# arquivo.py

if False:
   num = 2/"2"
else:
    num = 0
print(num)
```

```sh
python3 arquivo.py
```

<p align="center">
  <img src="../img/interpretada.png" />
</p>

Outra forma de gerar programas é a partir de linguagens compiladas. Um programa chamado compilador lê o código e o traduz completamente antes da execução. Após a etapa de compilação você pode executar repetidamente o programa sem que precise de nova tradução/interpretação.

<p align="center">
  <img src="../img/compile.png" />
</p>

A linguagem Python internamente utiliza os processos, mas devido a forma com que você interage com essa linguagem, ela é em geral considerada uma linguagem interpretada. O código fonte é primeiramente compilado para uma linguagem de baixo nível, chamado de código em bytes ("byte code"), e então são interpretados por um programa chamado de máquina virtual.

<p align="center">
  <img src="../img/python-compile-interpreted.png" />
</p>

### Tipagem dinâmica

O Python usa tipagem dinâmica, o que significa que você pode atribuir e reatribuir uma variável àa diferentes tipos de dados. Isso torna o Python muito flexível na atribuição de tipos de dados; ela difere de outras linguagens que são tipadas estaticamente.

```python
# Python

# Atribuindo um inteiro à variável num
num = 3
print(num)

# Reatribuindo a lista dee inteiros à variável num
num = "1"
print(num)
```

Outras linguagens exigem que você especifique o tipo antes de criar uma variável para armazenar valores. A linguagem Java é estaticamente tipada.

```java
// Java

String fruta = "Laranja"
fruta = 1 // Exception
```

A tipagem dinâmica é mais fácil de trabalhar e possibilita que o tempo de desenvolvimento para pequenos programas seja mais rápido. Porém, pode resultar em bugs inesperados e em alguns momentos você precisa usar a função type().

### Fortemente tipada

Python é uma linguagem fortemente tipada, o que significa que o interpretador não faz conversões automáticas ou coersões. O programa feito em Python necessita de um tipo exato para realizar as operações. O interpretador faz uma verificação no conteúdo das variáveis no momento da execução de uma instrução. Esta verificação é consequência da tipagem dinâmica, pois nenhuma verificação foi feita anteriormente e nenhuma conversão é automática. Isso afeta o desempenho da execução em aplicações de _extremo_ processamento.

A linguagem Javascript tenta realizar conversões para executar uma operação. Isso é uma característica de linguagem fracamenta tipada.

```javascript
// Javascript

2 / "2";
1;
```

Este mesmo código em Python resultará em um erro de tipo, pois a operação só pode ser realizada entre números.

```python
# Python

2 / "2";
TypeError
```

A partir da versão 3.6 a linguagem possibilita anotações de tipos para melhor identificar o funcionamento do código. Além dos tipos básicos ainda há um módulo que pode ser importado para isso: typing

```python
# Python

from typing import List
num: int = 3
numeros: List = [1,2,3]
def soma(a:int, b:int)-> int:
    return a+b
```

Adicinar anotações de tipo não é uma obrigação na linguagem Python, mas pode documentar e ajudar quando trabalhamos com código longo, evitando erros e mantendo os tipos sem variações.

![Plano Carteziano.](../img/tipagem.jpg)

### Duck Typing

Outro termo usado para descrever a tipagem em Python é o _Duck Typing_. Pelo conceito: "Se algo parece com um pato, faz barulho de pato ou anda como um pato, então deve ser um pato".

Este conceito não observa o tipo de um objeto, apenas se ele é capaz de realizar uma operação. Em um programa, se algo possui um método então pode ser usado para determinado fim, sem que haja verificação de tipo. Este conceito é utilizado nos métodos mágicos e nos métodos _dunder_.

Exempo: A função len() do Python calcula o comprimento de algo (Strings, Listas, etc.). Ela não existe um tipo, mas solicita que o que esteja sendo passado à ela saida dizer seu tamanho.

```python
# Python

nome = "Maria"
numeros = [1,2,3]
len(nome)       # 5
len(numeros)    # 3
```

### PEP 20 - Modo de Programar Python

A linguagem Python é construída a partir de proposta para melhoramento do Python discutidas entre a comunidade de programadores. Estas propostas são chamadas de [PEP's (Python Enhancement Proposal)](https://peps.python.org/pep-0001/). Duas PEP's muito importantantes para compreender a estrutura da linguagem são a [PEP20](https://peps.python.org/pep-0020/) (estilo) e a [PEP8](https://peps.python.org/pep-0008/) (formatação). A PEP20 é chamada de modo Python de Programar e possui o seguinte conteúdo:

> Beautiful is better than ugly.\
> Explicit is better than implicit.\
> Simple is better than complex.\
> Complex is better than complicated.\
> Flat is better than nested.\
> Sparse is better than dense.\
> Readability counts.\
> Special cases aren't special enough to break the rules.\
> Although practicality beats purity.\
> Errors should never pass silently.\
> Unless explicitly silenced.\
> In the face of ambiguity, refuse the temptation to guess.\
> There should be one-- and preferably only one --obvious way to do it.\
> Although that way may not be obvious at first unless you're Dutch.\
> Now is better than never.\
> Although never is often better than _right_ now.\
> If the implementation is hard to explain, it's a bad idea.\
> If the implementation is easy to explain, it may be a good idea.\
> Namespaces are one honking great idea -- let's do more of those!

# Versões da linguagem

Com a evolução da linguagem são adicionadas novas funcionalidades, melhorias de desempenho e ferramentas para auxiliar no desenvolvimento. A seguir estão algumas versões e datas de lançamento. Veja o destaque para a documentação da versão 2.7, que foi muito utilizada e para a versão atual (3.11).

- Python 1.0 - Jan 1994
- Python 2.0 - Out 2000.
- [Python 2.7](https://docs.python.org/2.7/) - Jan 2010
- Python 3.0 - Dez 2008
- [Python 3.11.4](https://docs.python.org/3.11/) - Jun 2023.

Cada versão possui um ciclo de atualizações que é mantida por um período de tempo.
Essas atualizações podem ser para resolver bugs ou problemas de segurança. Atualizações menores, como da versão 3.11.1 para a 3.11.2 resolvem pequenos problemas. Novas funcionalidades são inseridas em versões maiores, como por exemplo: A mudança da versão 3.10 para 3.11 ocorre adição de funcionalidades propostas e aprovadas em PEP's.

![Versões Python](../img/python-versions.png)

Quando temos diferentes projetos que usam a linguagem Python é comum criarmos ambientes virtuais para a execução separada, assim as bibliotecas e versões de outros projetos não entram em conflito.

![Ambientes Virtuais Python](../img/venv.png)

Para a versão 3.6+ estes ambientes virutais são criados com o comando.

```sh
python -m venv .venv
source .env/bin/activate
```

Para a versão 2.7 estes ambientes virutais são criados com o comando.

```sh
virtualenv -p /usr/bin/python2 env
source env/bin/activate
```

# Utilização e Ferramentas

Para construir programas mais complexos e que possuem muitas funcionalidades é comum utilizar ferramentas e bibliotecas que auxiliam no desenvolvimento pois já possuem várias funções prontas. Na linguagem Python existem diversos projetos de ferramentas e bibliotecas que você deve conhecer para programas maiores:

## Web Development

Desenvolver aplicações web com Python é uma das habilidades mais procuradas, com muitas oportunidades disponíveis para você. Nesse campo, você encontrará vários frameworks, bibliotecas e ferramentas úteis em Python para desenvolver aplicações web, APIs e muito mais. Aqui estão alguns dos frameworks web Python mais populares:

- Django: Django é um framework de alto nível que incentiva o desenvolvimento rápido de aplicações web com um design limpo e pragmático. Ele permite que você se concentre em escrever suas aplicações sem precisar reinventar a roda.

- FastAPI: FastAPI é um framework web rápido e eficiente para construir APIs web. Ele é construído em cima dos recursos modernos de dicas de tipos do Python e permite programação assíncrona.

- Flask: Flask é um framework leve para criar aplicações web WSGI. Ele permite que você comece rapidamente e possa escalar para aplicações complexas, se necessário.

## CLI Development

Outro campo em que o Python se destaca é o desenvolvimento de aplicativos de interface de linha de comando (CLI). Aplicativos CLI estão em todos os lugares e permitem automatizar tarefas repetitivas e tediosas no seu trabalho diário, criando ferramentas pequenas e grandes para a linha de comando.

Em Python, você tem um conjunto impressionante de bibliotecas e frameworks para CLI que podem tornar sua vida mais agradável e ajudá-lo a construir ferramentas de linha de comando rapidamente:

- argparse: argparse é um módulo da biblioteca padrão que permite escrever interfaces de linha de comando amigáveis ao usuário. Você pode definir os argumentos que deseja receber na linha de comando e analisá-los de forma clara. Ele gera automaticamente mensagens de ajuda e uso, além de emitir erros quando os usuários fornecem entradas inválidas.

- Click: Click é um pacote Python para criar interfaces de linha de comando bonitas com o mínimo de código necessário. É altamente configurável e vem com padrões sensatos prontos para uso. Seus objetivos incluem tornar o processo de escrever ferramentas de linha de comando rápido e divertido.

- Typer: Typer é uma biblioteca para construir aplicativos CLI que os usuários adorarão usar e os desenvolvedores adorarão criar. Ele fornece mensagens de ajuda automáticas e conclusão automática para todos os shells. Ele minimiza a duplicação de código e facilita a depuração.

## GUI Development

Aplicativos de interface gráfica do usuário (GUI) tradicionais para ambientes de desktop também são uma opção atraente em Python. Se você está interessado em construir esse tipo de aplicativo, o Python tem várias opções de bibliotecas, frameworks e conjuntos de ferramentas para escolher:

- Kivy: Kivy é uma biblioteca para desenvolvimento rápido de aplicativos com interfaces de usuário inovadoras, como aplicações multi-touch. Ele é executado no Linux, Windows, macOS, Android, iOS e Raspberry Pi.

- PyQt: PyQt é um conjunto de bindings Python para o framework de aplicativos Qt. Ele inclui classes para construir aplicativos GUI. Também fornece classes para rede, threads, bancos de dados SQL e muito mais. Ele suporta as plataformas Windows, Linux e macOS.

- tkinter: tkinter é uma interface Python padrão para o toolkit GUI Tk. Ele permite que você construa aplicativos GUI sem a necessidade de dependências de terceiros. Está disponível na maioria das plataformas Unix, bem como em sistemas Windows.

## Game Development

Criar jogos de computador é uma ótima maneira de aprender a programar não apenas em Python, mas também em qualquer outra linguagem. Para desenvolver jogos, você precisará usar variáveis, loops, declarações condicionais, funções, programação orientada a objetos e muito mais. O desenvolvimento de jogos é uma excelente opção para integrar várias habilidades.

Você encontrará várias ferramentas, bibliotecas e frameworks no ecossistema do Python para criar jogos rapidamente. Aqui está uma pequena amostra deles:

- Arcade: Arcade é uma biblioteca Python para criar jogos de vídeo 2D. É ideal para pessoas que estão aprendendo a programar, pois não precisam aprender um framework de jogos complexo para começar a criar seus próprios jogos.

- PyGame: PyGame é um conjunto de módulos Python projetados para escrever jogos de vídeo. Ele adiciona funcionalidades em cima da biblioteca SDL. Permite que você crie jogos completos e programas multimídia. A biblioteca é altamente portátil e roda em várias plataformas e sistemas operacionais.

- pyglet: pyglet é uma poderosa biblioteca Python para criar jogos e outras aplicações visualmente ricas no Windows, macOS e Linux. Ele suporta criação de janelas, manipulação de eventos de interface do usuário, gráficos OpenGL, carregamento de imagens, reprodução de vídeos e músicas.

## Machine Learning

A aprendizagem de máquina pode ser o primeiro passo para alguém interessado em inteligência artificial. A aprendizagem de máquina estuda algoritmos que aprendem por meio da experiência. Esses algoritmos constroem modelos com base em amostras de dados de treinamento para fazer previsões e tomar decisões.

- Keras: Keras é um framework de aprendizado profundo de alta qualidade com uma API projetada para ser amigável aos seres humanos. Ele permite que você execute novos experimentos e experimente ideias rapidamente. Segue as melhores práticas para reduzir a carga cognitiva.

- NLTK: NLTK é uma plataforma para construir programas Python para trabalhar com dados de linguagem humana. Ele fornece bibliotecas para classificação, tokenização, stemming, marcação, análise e raciocínio semântico.

- PyTorch: PyTorch é um framework de aprendizado de máquina de código aberto que acelera o caminho desde o protótipo de pesquisa até a implantação em produção.

- scikit-learn: scikit-learn é uma biblioteca de aprendizado de máquina de código aberto que suporta aprendizado supervisionado e não supervisionado. É uma ferramenta eficiente para análise preditiva de dados que é acessível a todos e reutilizável em vários contextos.

- TensorFlow: TensorFlow é uma plataforma de código aberto de ponta a ponta para aprendizado de máquina. Possui um ecossistema abrangente e flexível de ferramentas, bibliotecas e recursos da comunidade que o ajudarão a construir e implantar aplicativos com potência de ML.

## Computação Científica/Ciência de Dados

- [Numpy](https://numpy.org/): Pacote para computação científica que possui diversas funções de matemática, algebra linear e transofrmações de Fourier.
- [Scipy](https://www.scipy.org/): Pacote para computação com recursos para física, matemática e engenharia.
- [SimPy](https://simpy.readthedocs.io/en/latest/): Framwork para simulação de eventos. Pode simular aeroportos, rodovias, atendimentos ao cliente, etc.

## Data Analysis and Visualization

- Matplotlib: Uma biblioteca para criar visualizações de dados estáticas, animadas e interativas em Python.

- pandas: pandas é uma ferramenta poderosa e flexível de código aberto para análise e manipulação de dados. Ele fornece estruturas de dados rápidas, flexíveis e expressivas para trabalhar com dados relacionais ou rotulados.

- Seaborn: Biblioteca de visualização de dados baseada no Matplotlib. Ela fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos que permitem explorar e entender seus dados. Ela se integra de forma próxima com as estruturas de dados do pandas.

## Webscrapping

- [Beautiful](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Soup: Biblioteca python para recuperar dados de arquivos HTML e XML. Possibilita navegação, pesquisa, modificação e recuperação de informações no formato de árvores.
- [Requests](https://requests.readthedocs.io/en/latest/): Biblioteca python para recuperar conteúdo acesado via HTTP de forma simples.
- [Scrapy](https://docs.scrapy.org/en/latest/): Framework para realizar webcrawling em páginas web

## Devops

- [Ansible](https://www.ansible.com/): Ferramenta feita em Python para configurar, gerenciar e implantar aplicações. Segue o conceito de infraestrutura a partir do código.
- [Docker Compose](https://docs.docker.com/compose/): Ferramenta para criar e executar múltiplos containers Docker. A configuração é feita com um arquivo de descrição YAML e a ferramenta realiza os passos descritos.

## Software Testing

- doctest: doctest é um módulo padrão que busca suas docstrings por trechos de texto que se parecem com sessões interativas do Python e os executa para verificar se eles funcionam corretamente.

- pytest: pytest é um framework de teste robusto e maduro que permite que você escreva e automatize testes. Ele pode ser usado desde pequenos testes unitários até testes funcionais complexos para suas aplicações e bibliotecas.

## Banco de Dados

- sqlite3: sqlite3 é um banco de dados leve baseado em disco que não requer um processo de servidor separado. Ele permite que você acesse bancos de dados usando uma variante não padrão de SQL. Ele está disponível gratuitamente e faz parte da biblioteca padrão do Python.

- SQLAlchemys: SQLAlchemys é um kit de ferramentas SQL para Python e um mapeador objeto-relacional para bancos de dados SQL.

- MongoEngine: MongoEngine é um mapeador de documentos para trabalhar com o MongoDB usando programação orientada a objetos em Python.

- MySQL Connector/Python: MySQL Connector/Python é um driver Python autocontido para se comunicar com servidores MySQL.

## Software Packaging and Deployment

- Flit: Uma ferramenta que oferece uma maneira rápida de colocar seus pacotes e módulos Python no PyPI. Ela ajuda a configurar as informações sobre o seu pacote, para que você possa publicá-lo no PyPI com esforço mínimo.

- Poetry: Poetry é uma ferramenta para criar, construir, instalar e empacotar projetos Python. Ele também permite que você publique seus projetos no PyPI. Ele rastreia e resolve as dependências do seu projeto. Usa seus ambientes virtuais atuais ou cria novos para isolar seus pacotes da instalação do Python no sistema.

- PyInstaller: PyInstaller é uma ferramenta que transforma aplicações Python em executáveis independentes que funcionam no Windows, GNU/Linux, macOS e outros sistemas.

# Exercício

Faça uma pesquisa sobre as empresas que utilizam Python e as vagas de emprego existentes. Pesquisa os requisitos e faixa salarial.

# Referências

[Python Type Checking (Guide)](https://realpython.com/python-type-checking/)

[Linguagens Formais e Naturais](https://runestone.academy/ns/books/published/thinkcspy/GeneralIntro/FormalandNaturalLanguages.html)

[Versões do Python](https://www.python.org/doc/versions/)
