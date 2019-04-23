---
title: Jupyter Config
---

# Jupyter Config

The Notebook server runs the language kernel and communicates with the front-end Notebook client (i.e. the familiar notebook interface).

To create a jupyter_notebook_config.py file in the .jupyter directory, with all the defaults commented out, use the following command:

```bash
jupyter notebook --generate-config
```

`Command line arguments for configuration <config>` settings are documented in the configuration file and the user documentation.

## Examples

```bash
echo http://localhost:8010
CONF=base-url && \
  jupyter \
    notebook \
    --JupyterApp.config_file=$DLAHOME/etc/conf/_template/jupyter/${CONF}/jupyter_notebook_config.py \
    --NotebookApp.notebook_dir=~/notebooks \
    --log-level=DEBUG \
    --port 8010
```
