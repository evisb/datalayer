[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# JupyterLab Examples

[JupyterLab](https://github.com/jupyterlab/jupyterlab) examples [docs](https://jupyterlab.readthedocs.io/en/latest/developer/examples.html).

See also PR [Add some functionality to the notebook example](https://github.com/jupyterlab/jupyterlab/pull/5833).

```bash
# cell example.
cd $DLAHOME/etc/jupyterlab/examples/cell && \
  yarn install && \
  yarn build && \
  python main.py
# console example.
cd $DLAHOME/etc/jupyterlab/examples/console && \
  yarn install && \
  yarn build && \
  python main.py
# filebrowser example.
cd $DLAHOME/etc/jupyterlab/examples/filebrowser && \
  yarn install && \
  yarn build && \
  python main.py
# notebook example.
cd $DLAHOME/etc/jupyterlab/examples/notebook && \
  yarn install && \
  yarn build && \
  python main.py
# app example.
cd $DLAHOME/etc/jupyterlab/examples/app && \
  yarn install && \
  yarn build && \
  python main.py
# terminal example.
cd $DLAHOME/etc/jupyterlab/examples/terminal && \
  yarn install && \
  yarn build && \
  python main.py
# vega example.
# cd $DLAHOME/etc/jupyterlab/examples/vega && \
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
