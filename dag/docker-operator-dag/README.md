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

### 2. Local Development

Test the DAG locally without Airflow:

```bash
# Execute the DAG tasks locally
bazel run //dag/docker-operator-dag:local_dev
```

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
