# Docker Operator DAG with Bazel

```
docker-operator-dag/
├── BUILD.bazel      # Bazel build rules
├── dag.py           # Airflow DAG definition
├── local_dev.py     # Local execution script
├── task.py          # Python task to run in container
```

Build the container image

    bazel build //dag/docker-operator-dag:image

Load the image into Docker

    bazel run //dag/docker-operator-dag:image_load

Test the DAG locally without Airflow (uv method):

    uv run dag/docker-operator-dag/local_dev.py

Verify the image loaded correctly:

    docker images | grep docker-operator-dag

Test the container manually:

    docker run --rm docker-operator-dag:latest

Check Bazel outputs:

    bazel query //dag/docker-operator-dag:all --output=build
