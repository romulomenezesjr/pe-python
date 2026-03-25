# Módulos para desenvolvimento web


Python tem vários frameworks para desenvolvimento web, sendo os mais populares FastAPI, Flask e Django. Cada um tem suas características e casos de uso específicos. Vamos ver as diferenças entre eles.

- FastAPI – Rápido e Moderno
Normalmente utilizado para APIs, aplicações assíncronas e de alto desempenho. Ele éfocado em performance, utiliza o módulos com tipagem do Python para validação automática. Possui suporte nativo a OpenAPI e Swagger e possui o melhor desempenho entre os três.

- Flask – Leve e Flexível
Normalmente utilizando em aplicações pequenas/médias, APIs simples, microservices. Possui como características ser minimalista (só traz o essencial), flexível (você escolhe quais bibliotecas usar), boa documentação e fácil aprendizado para iniciantes.

- Django – Completo e Escalável
Normalmente utilizado em aplicações grandes, sistemas com banco de dados robustos, aplicações empresariais. Ele possui muitas ferramentas e módulos embutido (ORM, autenticação, admin, etc.). Já possui uma arquitetura pré-definida (padrão MTV - Model-Template-View). Entretanto pode ser "pesado" para projetos pequenos e tem uma curva de aprendizado maior.



## Utilização

Cada tutorial a seguir foi extraído da documentação oficial dos módulos.




### Fastapi

#### Passo 1 - Criar venv

```sh
python -m venv venv
```

#### Passo 2 - Habilitar a venv
```sh
meu_ambiente\Scripts\activate

```
#### Passo 3 - Instalar o fastapi
```sh
pip install "fastapi[standard]"
```

#### Passo 4 - Criar um arquivo main.py


O arquivo FastAPI mais simples pode conter o conteúdo a seguir:


```py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

FastAPI é uma classe Python que fornece todas as funcionalidades para sua API. A variável app será uma "instância" da classe FastAPI e  será o principal ponto de interação para criar toda a sua API.


Ao construir APIs, você normalmente usa esses métodos HTTP para executar uma ação específica.

- POST: para criar dados.
- GET: para ler dados.
- PUT: para atualizar dados.
- DELETE: para deletar dados.

O @app.get("/") diz ao FastAPI que a função logo abaixo é responsável por tratar as requisições que vão para a rota /.

#### Passo 5 - Execute 

No terminal utilize a ferramenta instala para executar o arquivo em modo de desenvolvimento

```sh
fastapi dev main.py
```

#### Passo 6 - Visualizar

Abra o seu navegador em http://127.0.0.1:8000.

```json
{"message": "Hello World"}
```

#### Passo 7 - Acessar documentação

O fastapi gera uma documentação para o projeto utilizando um módulo chamado swagger. Você pode acessá-lo 
 em http://127.0.0.1:8000/docs

![](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Flask

### Django

#### Passo 1 - Criar venv

```sh
python -m venv venv
```

#### Passo 2 - Habilitar a venv
```sh
meu_ambiente\Scripts\activate

```
#### Passo 3 - Instalar o django
```sh
pip install "Django"
```
