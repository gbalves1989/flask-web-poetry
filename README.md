# flask-web-poetry
[![codecov](https://codecov.io/gh/gbalves1989/flask-poetry/branch/main/graph/badge.svg?token=8BJ02V70OK)](https://codecov.io/gh/gbalves1989/flask-web-poetry)
[![Pipeline](https://github.com/gbalves1989/flask-poetry/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/gbalves1989/flask-poetry/actions/workflows/pipeline.yaml)

## Website desenvolvido em python com flask.
- Gerenciador de dependências com poetry
- Testes usando unittest
- CI/CD Github Actions
- Cobertura de testes usando Codecov 

## Testar aplicação localmente
- Adicionar um arquivo .env
  - SQLALCHEMY_DATABASE_URI= Ex.(postgresql://usuario:senha@host:porta/nome-do-banco) 
  - SQLALCHEMY_TRACK_MODIFICATIONS=False -> True ou False
  - SECRET_KEY= (sua key)
  - UPLOAD_FOLDER= Nome da pasta onde os avatares serão guardados no projeto no diretório static

- Instalar o ambiente de desenvolvimento:
  - python -m venv venv
  - cd venv/Scripts
  - .\activate
  
- Instalação dos pacotes do gerenciador do poetry:
  - pip install poetry
  - poetry install

- Criando as migrações: 
  - Antes de rodar a migração criar o banco denifinido acima
  - task init
  - task migrate
  - task upgrade 

- Executando os testes de cobertura localmente
  - task test
  - para acessar o arquivo html gerado entrar no diretório do projeto e abrir no navegador /htmlcov/index.html

- Executando a aplicação
  - task run
  - Acessar o link -> http://localhost:5000
