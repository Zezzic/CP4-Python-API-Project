# Catalogo de Jogos de Cartucho

Projeto de API em Python com FastAPI, banco SQLite e interface web em HTML, CSS e JavaScript puro.

## Modelos

- **Desenvolvedora**: id, nome, pais, ano_fundacao
- **Jogo**: id, titulo, console, ano, desenvolvedora_id

Relacao 1 para N: uma desenvolvedora possui varios jogos.

## Como instalar e executar

Pré-requisito: ter o Python 3 instalado na máquina (pode conferir rodando `python --version` ou `python3 --version` no terminal).

Os passos abaixo devem ser executados no terminal, dentro da pasta raiz do projeto (a pasta onde está o arquivo `main.py`).

### 1. Criar o ambiente virtual (venv)

O ambiente virtual isola as dependências do projeto do restante do sistema, evitando conflitos com outras instalações de Python na máquina. Esse passo só precisa ser feito uma vez.

```bash
py -m venv venv
```

Isso vai criar uma pasta chamada `venv` dentro do projeto. Se o comando `python` não funcionar, tente `python3`.

### 2. Ativar o ambiente virtual

Esse passo precisa ser repetido toda vez que for abrir um novo terminal para trabalhar no projeto.

```bash
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux ou Mac
```

Quando ativado corretamente, o nome `(venv)` vai aparecer no início da linha do terminal.

> Caso o Windows bloqueie a ativação com um erro de política de execução (execution policy), abra o PowerShell como administrador e rode `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`, depois tente ativar novamente.

### 3. Instalar as dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias (FastAPI, Uvicorn, etc.) listadas em `requirements.txt`:

```bash
pip install -r requirements.txt
```

Esse passo também só precisa ser feito uma vez por ambiente virtual (repetir apenas se o `requirements.txt` mudar).

### 4. Executar o projeto

Com as dependências instaladas e o ambiente virtual ainda ativado, suba o servidor:

```bash
uvicorn main:app --reload
```

A flag `--reload` reinicia o servidor automaticamente sempre que um arquivo do código é alterado, útil durante o desenvolvimento.

Se tudo der certo, o terminal vai mostrar uma mensagem como `Uvicorn running on http://127.0.0.1:8000`. Com o servidor rodando, acesse no navegador:

- **Interface web:** http://127.0.0.1:8000
- **Documentação automática (Swagger):** http://127.0.0.1:8000/docs

O arquivo `catalogo.db` (banco de dados SQLite) é criado automaticamente na primeira execução — não é necessário criar ou configurar nada manualmente.

Para parar o servidor, use `Ctrl + C` no terminal. Para sair do ambiente virtual quando terminar de usar o projeto, rode o comando `deactivate`.

## Endpoints

| Metodo | Rota | O que faz |
|---|---|---|
| GET | /desenvolvedoras | lista todas |
| GET | /desenvolvedoras/{id} | busca uma |
| POST | /desenvolvedoras | cadastra |
| PUT | /desenvolvedoras/{id} | atualiza |
| DELETE | /desenvolvedoras/{id} | remove |
| GET | /jogos | lista todos (com o nome da desenvolvedora) |
| GET | /jogos/{id} | busca um |
| POST | /jogos | cadastra |
| PUT | /jogos/{id} | atualiza |
| DELETE | /jogos/{id} | remove |

## Nome e RM dos Integrantes

- Diego Candido Stoianof — RM570748
- Felipe Moreira Mendes — RM570807
- Lucas Zezzi Custodio — RM571161
- Romulo Mendes Souza — RM570620
