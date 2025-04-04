Veja [python-pyproject-toml-uv-bazel](https://github.com/gpupo/python-pyproject-toml-uv-bazel/)

Build

    bazel build //packages/snakesay/src/snakesay:all

Run

    bazel run //packages/snakesay/src/snakesay:snakesay -- 'Hello, Bazel!'

UV

    uv build packages/snakesay


    uv pip install -e .

```
 _______________
( Hello, Bazel! )
 _______________
  \
   \    ___
    \  (o o)
        \_/ \
         λ \ \
           _\ \_
          (_____)_
         (________)=Oo°

```
