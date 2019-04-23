---
title: Jupyter Notebook
---

# Jupyter Notebook

[Notebook Docs](https://jupyter-notebook.readthedocs.io).

[Notebook Repository](https://github.com/jupyter/notebook).

```bash
echo http://localhost:8000
jupyter notebook
jupyter notebook --version
jupyter notebook --log-level DEBUG --port 8081
jupyter notebook list
jupyter notebook list --jsonlist
```

```python
from notebook import notebookapp
servers = list(notebookapp.list_running_servers())
print(servers)
```

## Runtime

```bash
jupyter --runtime-dir
find `jupyter --runtime-dir` -mtime -5 | grep nbserver | xargs cat
```

## Docker

```bash
docker run -it --rm -p 8888:8888 jupyter/scipy-notebook:8a1b90cbcba5
open http://localhost:8888
```

## Troubleshoot

```bash
jupyter troubleshoot
```

## Build

```bash
pip install -e .
npm run build
npm run build:watch
```

## Server

```python
# List running servers.
from notebook import notebookapp
servers = list(notebookapp.list_running_servers())
print servers
```
