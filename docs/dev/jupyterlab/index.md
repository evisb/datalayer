---
title: JupyterLab
---

# JupyterLab

## Source Code

Clone the JupyterLab [repository](https://github.com/jupyterlab/jupyterlab) and read the JupyterLab [docs](https://jupyterlab.readthedocs.io).

Check the [CI/CD](https://dev.azure.com/jupyterlab/jupyterlab) status.

## Community

[Weekly Dev Meetings](https://jupyter.readthedocs.io/en/latest/community/content-community.html#weekly-dev-meeting).

## Install

```bash
# pip install --upgrade jupyterlab
conda install -y jupyterlab && \
  jupyter lab
```

```bash
jupyter serverextension enable --py jupyterlab --sys-prefix && \
  jupyter lab
```

## Modes

### Core Mode

`--core-mode`: In this mode JupyterLab will run using the JavaScript assets contained in the installed `jupyterlab` Python package. In core mode, no extensions are enabled. This is the default in a stable JupyterLab release if you have no extensions installed.

### Dev Mode

`--dev-mode`: Uses the unpublished local JavaScript packages in the `dev_mode` folder.  In this case JupyterLab will show a red stripe at the top of the page.  It can only be used if JupyterLab is installed as `pip install -e .`.

### App Mode 

`--app-dir`: JupyterLab allows multiple JupyterLab "applications" to be created by the user with different combinations of extensions. The `--app-dir` can be used to set a directory for different applications. The default application path can be found using `jupyter lab path`.

## Paths

```bash
jupyter lab paths
```

## Awesome

https://github.com/mauhai/awesome-jupyterlab

## Keyboard Shortcuts

https://github.com/jupyterlab/jupyterlab/issues/2976

```bash
# https://blog.ja-ke.tech/2019/01/20/jupyterlab-shortcuts.html
# https://raw.githubusercontent.com/Jakeler/jupyter-shortcuts/master/outputs/Shortcuts.png
# https://raw.githubusercontent.com/Jakeler/jupyter-shortcuts/master/outputs/Shortcuts.pdf
git clone https://github.com/jakeler/jupyter-shortcuts && \
  cd jupyter-shortcuts && \
  yarn install && \
  open http://0.0.0.0:3000 && \
  yarn start-default
```
