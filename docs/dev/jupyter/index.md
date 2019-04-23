---
title: Jupyter
---

# Jupyter

## Community

Clone the [Jupyter](https://github.com/jupyter/jupyter) repository.

Join the Jupyter [mailing lists](https://groups.google.com/forum/#!forum/jupyter) and [Discourse](https://discourse.jupyter.org).

[Weekly Dev Meetings](https://jupyter.readthedocs.io/en/latest/community/content-community.html#weekly-dev-meeting).

You may be interested in the [Notebook Enterprise Summit repository](https://github.com/nteract/nes).

## Examples

Try the [Jupyter examples](https://github.com/datalayer/datalayer/tree/master/etc/examples/jupyter).

## Architecture

```
jupyterhub binderhub nbgrader nbviewer dashboards
  jupyter_console qtconsole notebook nbconvert
      jupyter_core jupyter_client nbformat
              ipykernel ipywidgets
                    ipython
                   traitlets
```

## Awesome

https://github.com/markusschanta/awesome-jupyter

## Manager

https://github.com/jupyter/nbmanager
