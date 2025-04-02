# Docker Operator DAG with Bazel

This directory contains an Apache Airflow DAG that demonstrates how to use the `DockerOperator` with Bazel for containerized task execution.

## Overview

The implementation:

1. Packages a Python task into a Docker container using Bazel
2. Creates an Airflow DAG that runs the task in a container
3. Provides local development and testing capabilities

## Structure

```
docker-operator-dag/
├── BUILD.bazel      # Bazel build rules
├── dag.py           # Airflow DAG definition
├── Dockerfile       # Docker configuration (alternative to Bazel)
├── local_dev.py     # Local execution script
├── task.py          # Python task to run in container
└── README.md        # This documentation
```

## How It Works

### 1. Building the Container Image

The Bazel build system packages the Python task into a container:

```bash
# Build the container image
bazel build //dag/docker-operator-dag:image

# Load the image into Docker
bazel run //dag/docker-operator-dag:image_load
```

### 2. Running the DAG

The DAG (`dag.py`) uses `DockerOperator` to execute the task in the container:

```python
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    'docker_operator_example',
    default_args=default_args,
    schedule_interval=None
) as dag:

    run_task = DockerOperator(
        task_id='run_in_docker',
        image='docker-operator-dag:latest',  # Matches repo_tags in BUILD.bazel
        api_version='auto',
        auto_remove=True,
        command='python /app/task.py'
    )
```

### 3. Local Development

Test the DAG locally without Airflow:

```bash
# Execute the DAG tasks locally
bazel run //dag/docker-operator-dag:local_dev
```

## Key Components

### `task.py`

The Python script that runs inside the container. Modify this for your specific task logic.

### `BUILD.bazel`

Defines the build pipeline:

- Creates a Python binary from `task.py`
- Packages it into a tarball
- Builds an OCI container image
- Provides a load rule for local Docker

### `local_dev.py`

Provides a local execution environment that:

- Simulates Airflow's task execution
- Runs each task sequentially
- Provides basic logging

## Development Workflow

1. Edit `task.py` with your task logic
2. Build and load the container:
   ```bash
   bazel run //dag/docker-operator-dag:image_load
   ```
3. Test locally:
   ```bash
   bazel run //dag/docker-operator-dag:local_dev
   ```
4. Deploy to Airflow

## Customizing

1. To add Python dependencies:

   - Add to `requirements.txt` in project root
   - Include in `deps` in `BUILD.bazel`

2. To change the base image:
   - Update the `base` parameter in `oci_image` rule
   - Or modify the `Dockerfile` for custom builds

## Troubleshooting

If the container fails to run:

1. Verify the image loaded correctly:
   ```bash
   docker images | grep docker-operator-dag
   ```
2. Test the container manually:
   ```bash
   docker run --rm docker-operator-dag:latest
   ```
3. Check Bazel outputs:
   ```bash
   bazel query //dag/docker-operator-dag:all --output=build
   ```
