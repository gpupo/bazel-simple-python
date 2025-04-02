from datetime import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    "docker_operator_example",
    schedule=None,
    start_date=datetime(2023, 1, 1),
) as dag:
    """
    Execute a command inside a docker container.

    By default, a temporary directory is
    created on the host and mounted into a container to allow storing files
    that together exceed the default disk size of 10GB in a container.
    In this case The path to the mounted directory can be accessed
    via the environment variable ``AIRFLOW_TMP_DIR``.

    If the volume cannot be mounted, warning is printed and an attempt is made to execute the docker
    command without the temporary folder mounted. This is to make it works by default with remote docker
    engine or when you run docker-in-docker solution and temporary directory is not shared with the
    docker engine. Warning is printed in logs in this case.

    If you know you run DockerOperator with remote engine or via docker-in-docker
    you should set ``mount_tmp_dir`` parameter to False. In this case, you can still use
    ``mounts`` parameter to mount already existing named volumes in your Docker Engine
    to achieve similar capability where you can store files exceeding default disk size
    of the container,

    If a login to a private registry is required prior to pulling the image, a
    Docker connection needs to be configured in Airflow and the connection ID
    be provided with the parameter ``docker_conn_id``.

    :param image: Docker image from which to create the container.
        If image tag is omitted, "latest" will be used. (templated)
    :param api_version: Remote API version. Set to ``auto`` to automatically
        detect the server's version.
    :param command: Command to be run in the container. (templated)
    :param container_name: Name of the container. Optional (templated)
    :param cpus: Number of CPUs to assign to the container.
        This value gets multiplied with 1024. See
        https://docs.docker.com/engine/reference/run/#cpu-share-constraint
    :param docker_url: URL or list of URLs of the host(s) running the docker daemon.
        Default is the value of the ``DOCKER_HOST`` environment variable or unix://var/run/docker.sock
        if it is unset.
    :param environment: Environment variables to set in the container. (templated)
    :param private_environment: Private environment variables to set in the container.
        These are not templated, and hidden from the website.
    :param env_file: Relative path to the ``.env`` file with environment variables to set in the container.
        Overridden by variables in the environment parameter. (templated)
    :param force_pull: Pull the docker image on every run. Default is False.
    :param mem_limit: Maximum amount of memory the container can use.
        Either a float value, which represents the limit in bytes,
        or a string like ``128m`` or ``1g``.
    :param host_tmp_dir: Specify the location of the temporary directory on the host which will
        be mapped to tmp_dir. If not provided defaults to using the standard system temp directory.
    :param network_mode: Network mode for the container. It can be one of the following:

        - ``"bridge"``: Create new network stack for the container with default docker bridge network
        - ``"none"``: No networking for this container
        - ``"container:<name|id>"``: Use the network stack of another container specified via <name|id>
        - ``"host"``: Use the host network stack. Incompatible with `port_bindings`
        - ``"<network-name>|<network-id>"``: Connects the container to user created network
          (using ``docker network create`` command)
    :param tls_ca_cert: Path to a PEM-encoded certificate authority
        to secure the docker connection.
    :param tls_client_cert: Path to the PEM-encoded certificate
        used to authenticate docker client.
    :param tls_client_key: Path to the PEM-encoded key used to authenticate docker client.
    :param tls_verify: Set ``True`` to verify the validity of the provided certificate.
    :param tls_hostname: Hostname to match against
        the docker server certificate or False to disable the check.
    :param tls_ssl_version: Version of SSL to use when communicating with docker daemon.
    :param mount_tmp_dir: Specify whether the temporary directory should be bind-mounted
        from the host to the container. Defaults to True
    :param tmp_dir: Mount point inside the container to
        a temporary directory created on the host by the operator.
        The path is also made available via the environment variable
        ``AIRFLOW_TMP_DIR`` inside the container.
    :param user: Default user inside the docker container.
    :param mounts: List of volumes to mount into the container. Each item should
        be a :py:class:`docker.types.Mount` instance.
    :param entrypoint: Overwrite the default ENTRYPOINT of the image
    :param working_dir: Working directory to
        set on the container (equivalent to the -w switch the docker client)
    :param xcom_all: Push all the stdout or just the last line.
        The default is False (last line).
    :param docker_conn_id: The :ref:`Docker connection id <howto/connection:docker>`
    :param dns: Docker custom DNS servers
    :param dns_search: Docker custom DNS search domain
    :param auto_remove: Enable removal of the container when the container's process exits. Possible values:

        - ``never``: (default) do not remove container
        - ``success``: remove on success
        - ``force``: always remove container
    :param shm_size: Size of ``/dev/shm`` in bytes. The size must be
        greater than 0. If omitted uses system default.
    :param tty: Allocate pseudo-TTY to the container
        This needs to be set see logs of the Docker container.
    :param hostname: Optional hostname for the container.
    :param privileged: Give extended privileges to this container.
    :param cap_add: Include container capabilities
    :param extra_hosts: Additional hostnames to resolve inside the container,
        as a mapping of hostname to IP address.
    :param retrieve_output: Should this docker image consistently attempt to pull from and output
        file before manually shutting down the image. Useful for cases where users want a pickle serialized
        output that is not posted to logs
    :param retrieve_output_path: path for output file that will be retrieved and passed to xcom
    :param timeout: Timeout for API calls, in seconds. Default is 60 seconds.
    :param device_requests: Expose host resources such as GPUs to the container.
    :param log_opts_max_size: The maximum size of the log before it is rolled.
        A positive integer plus a modifier representing the unit of measure (k, m, or g).
        Eg: 10m or 1g Defaults to -1 (unlimited).
    :param log_opts_max_file: The maximum number of log files that can be present.
        If rolling the logs creates excess files, the oldest file is removed.
        Only effective when max-size is also set. A positive integer. Defaults to 1.
    :param ipc_mode: Set the IPC mode for the container.
    :param skip_on_exit_code: If task exits with this exit code, leave the task
        in ``skipped`` state (default: None). If set to ``None``, any non-zero
        exit code will be treated as a failure.
    :param port_bindings: Publish a container's port(s) to the host. It is a
        dictionary of value where the key indicates the port to open inside the container
        and value indicates the host port that binds to the container port.
        Incompatible with ``"host"`` in ``network_mode``.
    :param ulimits: List of ulimit options to set for the container. Each item should
        be a :py:class:`docker.types.Ulimit` instance.
    :param labels: A dictionary of name-value labels (e.g. ``{"label1": "value1", "label2": "value2"}``)
        or a list of names of labels to set with empty values (e.g. ``["label1", "label2"]``)
    """
    run_task = DockerOperator(
        task_id="run_in_docker",
        image="docker-operator-dag:latest",
        api_version="auto",
        # auto_remove=True,
        docker_url="unix:///var/run/docker.sock",  # Ou "tcp://localhost:2375"
        network_mode="bridge",
    )
