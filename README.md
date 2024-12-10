# OpenQP with Jupyter Notebook

## Quickstart

1. Pull the Docker image:
```
docker pull openqp/openqp:jupyter_notebook
```

2. Run the Docker container:
```
docker run -p 8888:8888 -v $(pwd):/data openqp/openqp:jupyter_notebook
```

3. Access Jupyter Notebook in your browser at `http://localhost:8888`.

## Example Files

- Find an example file in this repository.
- For more examples, visit: [Example Input Files](https://github.com/Open-Quantum-Platform/openqp/wiki/Example%20Input%20Files)
