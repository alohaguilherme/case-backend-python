# **Case Backend Python**
[![GitHub Actions CI](https://github.com/microsoft/TypeScript/workflows/CI/badge.svg)](https://github.com/alohaguilherme/case-backend-python/actions?query=workflow%3ACI) 
[![GitHub Actions CI](https://github.com/python/cpython/workflows/Tests/badge.svg)](https://github.com/alohaguilherme/case-backend-python/actions?query=workflow%3ACI) 
[![pyversion-button](https://img.shields.io/pypi/pyversions/Markdown.svg)]()

Este repositório tem por objetivo implementar conceitos de programação utilizando a linguagem Python.

## Conteudo
  - [Instalação](#instalação)
    - [Docker](#docker)
    - [Windows](#windows)
    - [Linux](#linux)
  - [Uso](#uso)
    - [Tests](#tests)
    - [API](#api)

## Instalação
---
> :warning: Neste projeto estamos utilizando ptyhon em versões >= 3.10.

- #### Docker
    > Para instalar o docker e docker compose acesse a documentação oficial respectivamente [Docker](https://docs.docker.com/engine/install/), [Docker-Compose](https://docs.docker.com/compose/install/)

    Se desejar utilizar por meio do docker ao clonar o repositório podera simplismente rodar o arquivo docker-compose.yaml com o comando abaixo
    ```bash
    docker-compose up -d --build
    ```
    isso irá buildar o arquivo Dockerfile.dev e subir um container e isso será o suficiente para começar a desenvolver, uma vez que a imagem já está configurada para instalar as libs por meio do package manager [PDM](https://pdm.fming.dev/latest/)
  <a id="windows"></a>
- ### Windows
    Diferente do linux o python não vem instalado por padrão no windows, então é necessario instalar manualmente, poderá acessar o executavel por esse link [python-install](https://www.python.org/downloads/)

    ao completar a instalação poderá abrir o terminal e instalar o package manager [PDM](https://pdm.fming.dev/latest/)
    ```bash
    pip install pdm
    pdm --pep582
    ```

    após realizar esse passo poderá ir no diretório onde salvou o repositório e executar o comando de instalação das libs
    ```bash
    pdm install
    ```
    agora estará com todas as libs do projeto instaladas.
   <a id="linux"></a>
- ### Linux/wsl/Desktop enviroment
    Como identificado acima, fique atendo a versão do python. verifique o python instalado em sua distro com os comandos abaixo:
    ```bash
    python --versions or python3 --version
    ```
    após verificar a versão poderá abrir o terminal e instalar o package manager [PDM](https://pdm.fming.dev/latest/)
    ```bash
    pip install pdm
    echo 'eval "$(pdm --pep582)"' >> ~/.bashrc
    ou 
    echo 'eval "$(pdm --pep582)"' >> ~/.zshrc
    ```

    após realizar esse passo poderá ir no diretório onde salvou o repositório e executar o comando de instalação das libs
    ```bash
    pdm install
    ```
    agora estará com todas as libs do projeto instaladas.

## Uso
---
- ### Tests
    Para rodar os teste da aplicação poderá verificar o diretório 
    > ./scripts
- ### Api
    A api segue os padrões descritos abaixo:
    
    * Body
    
        | Método | Rota         | Descricao                                 | Body                                                        | Retorno                             |
        | ------ | ------------ | ----------------------------------------- | ----------------------------------------------------------- | ----------------------------------- |
        | `POST`   | /SORT        | Ordena as palavras informadas             | ```{words: [ 'word1', 'word3','word2'], order: 'desc' / 'asc'}``` |   ```['word1', 'word2', 'word3']```         |  |
        | `POST`   | /VOWEL_COUNT | Conta a quantidade de vogais das palavras | ```{words: [ 'word1', 'word3','word2']}```                  | ```{word1:1, word2: 1, word3: 1```} |

    * Repostas
  
  
        | Código | Descrição                                                          |
        | ------ | ------------------------------------------------------------------ |
        | `200`  | Requisição executada com sucesso (success).                        |
        | `400`  | Erros de validação ou os campos informados não existem no sistema. |
        | `405`  | Método não implementado.                                           |
        | `415`  | Dados de acesso inválidos.                                         |
        | `500`  | Erros internos                                                     |
