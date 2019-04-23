---
title: Nteract Jupyter Extension
---

# Nteract Jupyter Extension

[Github Nteract](https://github.com/nteract/nteract).

[Nteract Jupyter Extension on Binder](https://mybinder.org/v2/gh/nteract/vdom/master?urlpath=nteract/edit/example-notebooks).

## Install

```bash
pip install nteract_on_jupyter && \
  jupyter serverextension enable nteract_on_jupyter && \
  jupyter serverextension list
jupyter nteract
```

## Build

```bash
echo http://localhost:8080
cd $DLAHOME/repos/nteract/applications/jupyter-extension && \
  pip install -e . && \
  jupyter serverextension enable nteract_on_jupyter && \
  jupyter serverextension list && \
  jupyter nteract # wait a bit for compilation...
#  jupyter nteract --dev
#  jupyter nteract --dev --watch
```

```bash
echo http://localhost:8080
cd $DLAHOME/repos/nteract && \
  yarn && \
  yarn app:jupyter-extension # wait a bit for compilation...
```
