[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# JupyterLab Datalayer

:rocket: JupyterLab Extension for Datalayer.

![JupyterLab Datalayer](https://raw.githubusercontent.com/datalayer/jupyterlab-datalayer/master/docs/jupyterlab-datalayer.gif "JupyterLab Datalayer")

> Replace `$DLAHOME/libs` in the following commands with whatever your local env looks like.

To start or develop, you first have to build `jupyterlab`.

```bash
# build jupyterlab.
cd $DLAHOME/repos/jupyterlab && \
  git checkout datalayer && \
  pip install -e . && \
  jupyter serverextension enable --py jupyterlab --sys-prefix && \
  yarn install && \
#  yarn clean && \
#  yarn install && \
  cd $DLAHOME/repos/jupyterlab/packages/cells && \
  yarn install && \
  yarn build && \
  jupyter lab build
```

You also have to build `jupyterlab-datalayer` extension and enable the extension.

```bash
# build and enable `jupyterlab-datalayer` extension.
cd $DLAHOME/apps/jupyterlab-datalayer && \
  make build && \
  make install && \
  make ext-enable && \
  jupyter lab build
```

Start jupyterlab with the `jupyterlab-datalayer` extension enables.

```bash
jupyter lab
```

## Develop

```bash
# prerequisite: install development version of the ui server.
cd $DLAHOME/apps/jupyterlab-datalayer && \
  python setup.py develop
```

```bash
# shell #1 - watch the extension.
cd $DLAHOME/apps/jupyterlab-datalayer && \
  make watch
# shell #2 - run and watch jupyter lab.
  # --dev-mode \
cd $DLAHOME/apps/jupyterlab-datalayer && \
  jupyter lab \
    --watch \
    --browser chromium-browser \
    --config ./jupyter_notebook_config.py
# shell #3 - list the notebooks.
jupyter notebook list
```

In case of issue (version mismatch...), try.

```bash
jupyter lab clean
jupyter lab build
```
