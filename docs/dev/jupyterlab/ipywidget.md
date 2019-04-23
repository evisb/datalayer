---
title: JupyterLab IpyWidget
---

# JupyterLab IpyWidget

All widgets do the same pattern including the core widgets, pythreejs, ipyleaflet, bqplot, etc.

Write the core widget once. Then there's a small shim that registers the widget in lab, and another small shim that makes it available as an nbextension

Pattern in the cookiecutter.

https://github.com/jupyter-widgets/widget-ts-cookiecutter/

Lab shim.

https://github.com/jupyter-widgets/widget-ts-cookiecutter/blob/master/%7B%7Bcookiecutter.github_project_name%7D%7D/src/plugin.ts

Part that packages up an nbextension.

https://github.com/jupyter-widgets/widget-ts-cookiecutter/blob/acb06b2b298608974d1b2ba66171ab83ec384c35/%7B%7Bcookiecutter.github_project_name%7D%7D/webpack.config.js#L11-L28

Part that tells lab where to look for the lab shim.

https://github.com/jupyter-widgets/widget-ts-cookiecutter/blob/acb06b2b298608974d1b2ba66171ab83ec384c35/%7B%7Bcookiecutter.github_project_name%7D%7D/package.json#L72-L74
