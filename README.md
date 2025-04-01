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

## Requisitos

- Python >= 3.13
- Bazel (bzlmod)
