---
title: Jupyter Extensions
---

# Jupyter Extensions

```bash
# nbextension: A notebook extension. A single JS file, or directory of JavaScript, Cascading StyleSheets, etc. that contain at minimum a JavaScript module packaged as an AMD modules that exports a function `load_ipython_extension`.
jupyter nbextension list
# server extension: An importable Python module that implements `load_jupyter_server_extension`.
jupyter serverextension list
# bundler extension: An importable Python module with generated File -> Download as / Deploy as menu item. trigger that implements bundle.
jupyter bundlerextension list
```

## Pizza Extension

```bash
# Pizza Extension.
pip install pizzabutton
jupyter serverextension enable --py pizzabutton --sys-prefix
jupyter nbextension install --py pizzabutton --sys-prefix
jupyter nbextension enable --py pizzabutton --sys-prefix
```

## Grader Extension

Clone the [Jupyter Grader](https://github.com/jupyter/nbgrader) repository and read the [Jupyter Grader](https://nbgrader.readthedocs.io) docs.

To run Grader on Jupyterhub, clone the [JupyterHub Deploy Teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching) repository and read the [JupyterHub Deploy Teaching](http://jupyterhub-deploy-teaching.readthedocs.io/en/latest) docs.
