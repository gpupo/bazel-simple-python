# Projeto de Exemplo: Monorepo com Python e Bazel

Este é um projeto de exemplo que demonstra o uso de [Bazel](https://bazel.build) para gerenciar um monorepo com Python.

## Estrutura do Projeto

```
.
├── bazel-bazel-simple  # Diretório gerado pelo Bazel
├── bazel-bin           # Saída dos builds
├── bazel-out           # Cache e artefatos do Bazel
├── bazel-testlogs      # Logs de testes
├── mylib/              # Módulo Python de exemplo
├── main.py             # Script principal
├── BUILD.bazel         # Configuração do Bazel
├── MODULE.bazel        # Definição do módulo Bazel
├── MODULE.bazel.lock   # Arquivo de bloqueio do módulo
├── pyproject.toml      # Configuração do projeto Python
├── requirements.txt    # Dependências do projeto
```

## Preparo do ambiente

    bazel run //:create_venv


    bazel run //:sync_venv

## Compilando

Para gerar o arquivo `requirements.txt` a partir do `pyproject.toml`, execute:

```sh
bazel run //:generate_requirements_txt
```

Para compilar o projeto, utilize o seguinte comando:

```sh
bazel build //...
```

Para rodar os testes do projeto, utilize:

```sh
bazel test //...
```

## Simple DAG Apache Airflow

Rodando os testes unitarios

    bazel run //dag/simple_dag:dag_test

Rodando a adaptacao para ambiente local

    bazel run //dag/simple_dag:dag_dev

## DockerOperator

    bazel build //dag/docker-operator-dag:python3_image

## Requisitos

- Python >= 3.12
- Bazel (bzlmod)

## Destaques

Dependencias usando constraints

```sh
 uv add "pytest"\
    "apache-airflow>=2.10.5"\
    "apache-airflow-providers-postgres"\
    "apache-airflow-providers-common-sql"\
    "apache-airflow-providers-sqlite"\
 --constraint deps/apache-airflow-2.10.5-constraints-python-3.12.txt
```
