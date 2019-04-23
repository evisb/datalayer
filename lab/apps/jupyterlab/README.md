[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# JupyterLab Lab

[JupyterLab](https://github.com/jupyterlab/jupyterlab) examples [docs](https://jupyterlab.readthedocs.io/en/latest/developer/examples.html).

See also PR [Add some functionality to the notebook example](https://github.com/jupyterlab/jupyterlab/pull/5833).

```bash
# cell example.
cd $DLAHOME/lab/apps/jupyterlab/cell && \
  yarn install && \
  yarn build && \
  python main.py
# console example.
cd $DLAHOME/lab/apps/jupyterlab/console && \
  yarn install && \
  yarn build && \
  python main.py
# filebrowser example.
cd $DLAHOME/lab/apps/jupyterlab/filebrowser && \
  yarn install && \
  yarn build && \
  python main.py
# notebook example.
cd $DLAHOME/lab/apps/jupyterlab/notebook && \
  yarn install && \
  yarn build && \
  python main.py
# app example.
cd $DLAHOME/lab/apps/jupyterlab/app && \
  yarn install && \
  yarn build && \
  python main.py
# terminal example.
cd $DLAHOME/lab/apps/jupyterlab/terminal && \
  yarn install && \
  yarn build && \
  python main.py
# vega example.
# cd $DLAHOME/lab/apps/jupyterlab/vega && \
#   yarn install && \
#   yarn build && \
#   python main.py
```

```bash
# Build the examples from the jupyterlab repository.
cd $DLAHOME/repos/jupyterlab && \
  git checkout tags/v0.35.4 -b v0.35.4 && \
  yarn install && \
  jupyter lab build && \
  yarn build:examples
```
